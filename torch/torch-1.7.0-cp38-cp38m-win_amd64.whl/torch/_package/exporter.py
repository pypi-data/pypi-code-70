import torch
from torch.serialization import normalize_storage_type, location_tag, _should_read_directly
import io
import pickle
import pickletools
from .find_file_dependencies import find_files_source_depends_on
from ._custom_import_pickler import CustomImportPickler
from ._importlib import _normalize_path
import types
import importlib
from typing import List, Any, Callable, Dict, Tuple
from distutils.sysconfig import get_python_lib
from pathlib import Path
import linecache
import sys
from tempfile import NamedTemporaryFile

class PackageExporter:
    """ Exporters allow you to write packages of code, pickled python data, and
    arbitrary binary and text resources into a self-contained package.

    Imports can load this code in a hermetic way, such that code is loaded
    from the package rather than the normal python import system. This allows
    for the packaging of PyTorch model code and data so that it can be run
    on a server or used in the future for transfer learning.

    The code contained in packages is copied file-by-file from the original
    source when it is created, and the file format is a specially organized
    zip file. Future users of the package can unzip the package, and edit the code
    in order to perform custom modifications to it.

    The importer for packages ensures that code in the module can only be loaded from
    within the package, except for modules explicitly listed as external using :method:`extern_module`.
    The file `extern_modules` in the zip archive lists all the modules that a package externally depends on.
    This prevents "implicit" dependencies where the package runs locally because it is importing
    a locally-installed package, but then fails when the package is copied to another machine.


    Dependencies
    ------------

    When source code is added to the package, the exporter optionally can scan it
    for further code dependencies (`dependencies=True`). It looks for import statements,
    resolves relative references to qualified module names, and calls :method:`require_module`
    on each it finds, recursively resolving dependencies.

    """

    importers: List[Callable[[str], Any]]
    """ A list of functions that will be called in order to find the module assocated
    with module names referenced by other modules or by pickled objects. Initialized to
    `[importlib.import_module]` by default. When pickling code or objects that was loaded
    from an imported packaged, that `importer.import_module` should be put into the importer list.
    When a name conflict occurs between importers, the first importer in the list takes precedence,
    and only objects that refer to this first importers class can be saved
    """


    def __init__(self, filename: str, verbose: bool = True):
        """
        Create an exporter.

        Args:
            filename: e.g. my_package.zip
            verbose: Print information about dependency resolution to stdout.
                Useful for tracking down why certain files get included.
        """
        self.zip_file = torch._C.PyTorchFileWriter(filename)
        self.serialized_storages : Dict[str, Any] = {}
        self.external : List[str] = []
        self.provided : Dict[str, bool] = {}
        self.verbose = verbose
        self.importers = [importlib.import_module]
        self.debug_deps : List[Tuple[str, str]] = []

    def save_source_file(self, module_name: str, file_or_directory: str, dependencies=True):
        """Adds the local file system `file_or_directory` to the source package to provide the code
        for `module_name`.

        Args:
            module_name (str): e.g. `my_package.my_subpackage`, code will be saved to provide code for this package.
            file_or_directory (str): the path to a file or directory of code. When a directory, all python files in the directory
                are recursively copied using :meth:`save_source_file`. If a file is named "/__init__.py" the code is treated
                as a package.
            dependencies (bool, optional): If True, we scan the source for dependencies (see :ref:`Dependencies`).
        """
        path = Path(file_or_directory)
        if path.is_dir():
            to_save = []  # list of tuples with arguments to save_source_string
            module_path = module_name.replace('.', '/')
            for filename in path.glob('**/*.py'):
                relative_path = filename.relative_to(path).as_posix()
                archivename = module_path + '/' + relative_path
                if filename.is_dir():
                    self.provided[archivename] = True
                else:
                    submodule_name = None
                    if filename.name == '__init__.py':
                        submodule_name = archivename[:-len('/__init__.py')].replace('/', '.')
                        is_package = True
                    else:
                        submodule_name = archivename[:-len('.py')].replace('/', '.')
                        is_package = False

                    self.provided[submodule_name] = True
                    # we delay the call to save_source_string so that we record all the source files
                    # being provided by this directory structure _before_ attempting to resolve the dependencies
                    # on the source. This makes sure we don't try to copy over modules that will just get
                    # overwritten by this directory blob
                    to_save.append((submodule_name, _read_file(str(filename)), is_package, dependencies, str(filename)))

            for item in to_save:
                self.save_source_string(*item)
        else:
            is_package = path.name == '__init__.py'
            self.save_source_string(module_name, _read_file(file_or_directory), is_package, dependencies, file_or_directory)

    def save_source_string(self, module_name: str, src: str, is_package: bool = False,
                           dependencies: bool = True, orig_file_name: str = None):
        """Adds `src` as the source code for `module_name` in the exported package.

        Args:
            module_name (str): e.g. `my_package.my_subpackage`, code will be saved to provide code for this package.
            src (str): The python source code to save for this package
            is_package (bool, optional): If True, this module is treated as a package. Packages are allowed to have submodules
                (e.g. my_package.my_subpackage.my_subsubpackage), and resources can be saved inside them. Defaults to False.
            dependencies (bool, optional): If True, we scan the source for dependencies (see :ref:`Dependencies`).
            orig_file_name (str, optional): If present, used in logging to identifying where the source came from. Defaults to None.
        """
        self.provided[module_name] = True
        extension = '/__init__.py' if is_package else '.py'
        filename = module_name.replace('.', '/') + extension
        self._write(filename, src)
        if dependencies:
            package = module_name if is_package else module_name.rsplit('.', maxsplit=1)[0]
            dep_pairs = find_files_source_depends_on(src, package)
            dep_list = {}
            for dep_module_name, dep_module_obj in dep_pairs:
                # handle the case where someone did something like `from pack import sub`
                # where `sub` is a submodule. In this case we don't have to save pack, just sub.
                # this ensures we don't pick up additional dependencies on pack.
                # However, in the case where `sub` is not a submodule but an object, then we do have
                # to save pack.
                if dep_module_obj is not None:
                    possible_submodule = f'{dep_module_name}.{dep_module_obj}'
                    if self._module_exists(possible_submodule):
                        dep_list[possible_submodule] = True
                        # we don't need to save `pack`
                        continue
                if self._module_exists(dep_module_name):
                    dep_list[dep_module_name] = True

            for dep in dep_list.keys():
                self.debug_deps.append((module_name, dep))

            if self.verbose:
                dep_str = ''.join(f'  {dep}\n' for dep in dep_list.keys())
                file_info = f'(from file {orig_file_name}) ' if orig_file_name is not None else ''
                print(f"{module_name} {file_info}depends on:\n{dep_str}\n")

            for dep in dep_list.keys():
                self.require_module_if_not_provided(dep)

    def _module_exists(self, module_name: str) -> bool:
        try:
            self._import_module(module_name)
            return True
        except Exception:
            return False

    def _write_dep_graph(self, failing_module=None, output_file=None):
        depended_on : Dict[str, List[str]] = {}
        for f, t in self.debug_deps:
            if t not in depended_on:
                depended_on[t] = []
            if f not in depended_on:
                depended_on[f] = []
            depended_on[t].append(f)

        level : Dict[str, int] = {}

        def visit(x: str):
            if x in level:
                return level[x]
            level[x] = 0
            for e in depended_on[x]:
                level[x] = max(level[x], visit(e) + 1)
            return level[x]

        for x in depended_on.keys():
            visit(x)

        nodes = []
        node_to_id = {}
        n = 0
        for ft in self.debug_deps:
            for e in ft:
                if e not in node_to_id:
                    node_to_id[e] = n
                    extra = ''
                    if e == failing_module:
                        extra = ", color: 'red'"
                    nodes.append(f"        {{id: {n}, label: '{e}', level: {level[e]}, shape: 'box'{extra}}},\n")
                    n += 1
        edges = []
        for f, t in self.debug_deps:
            fn, tn = node_to_id[f], node_to_id[t]
            edges.append(f"            {{from: {fn}, to: {tn}, arrows: 'to'}},\n")
        nodes_s, edges_s = ''.join(nodes), ''.join(edges)
        template = f"""\
<html>
<head>
    <script type="text/javascript" src="https://almende.github.io/vis/dist/vis.js"></script>
    <link href="https://almende.github.io/vis/dist/vis.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="mynetwork"></div>

<script type="text/javascript">
    var nodes = new vis.DataSet([
{nodes_s}
    ]);
    var edges = new vis.DataSet([
{edges_s}
    ]);
    var options = {{
        layout: {{
            hierarchical: {{
                direction: "LR",
                levelSeparation: 400,
            }},
        }},
    }};
    // create a network
    var container = document.getElementById('mynetwork');
    var network = new vis.Network(container, {{nodes: nodes, edges: edges}}, options);
</script>
</body>
</html>
"""
        if output_file:
            output_file.write(template)
            return None

        with NamedTemporaryFile(mode='w', suffix='.html', delete=False) as tf:
            tf.write(template)
            return tf.name

    def _get_source_of_module(self, module: types.ModuleType) -> str:
        filename = getattr(module, '__file__', None)
        result = None if filename is None or not filename.endswith('.py') else linecache.getlines(filename, module.__dict__)
        if result is None:
            extra = ''
            if self.verbose:
                extra = f' See the dependency graph for more info: {self._write_dep_graph(module.__name__)}'
            raise ValueError(f'cannot save source for module "{module.__name__}" because '
                             f'its source file "{filename}" could not be found.{extra}')
        return ''.join(result)

    def require_module_if_not_provided(self, module_name: str, dependencies=True):
        if self._module_is_already_provided(module_name):
            return
        self.require_module(module_name, dependencies)

    def require_module(self, module_name: str, dependencies=True):
        """This is called by dependencies resolution when it finds that something in the package
        depends on the module and it is not already present. It then decides how to provide that module.
        The default resolution rules will mark the module as extern if it is part of the standard library,
        and call `save_module` otherwise. Clients can subclass this object
        and override this method to provide other behavior, such as automatically mocking out a whole class
        of modules"""

        root_name = module_name.split('.', maxsplit=1)[0]
        if self._can_implicitly_extern(root_name):
            if self.verbose:
                print(f'implicitly adding {root_name} to external modules '
                      f'since it is part of the standard library and is a dependency.')
            self.extern_module(root_name)
            return

        self.save_module(module_name, dependencies)

    def save_module(self, module_name: str, dependencies=True):
        """Save the code for `module_name` into the package. Code for the module is resolved using the `importers` path to find the
        module object, and then using its `__file__` attribute to find the source code.
        Args:
            module_name (str): e.g. `my_package.my_subpackage`, code will be saved to provide code for this package.
            dependencies (bool, optional): If True, we scan the source for dependencies (see :ref:`Dependencies`).
        """
        module = self._import_module(module_name)
        source = self._get_source_of_module(module)
        self.save_source_string(module_name, source, hasattr(module, '__path__'), dependencies, module.__file__)


    def _import_module(self, module_name):
        last_err = None
        for import_module in self.importers:
            try:
                return import_module(module_name)
            except ModuleNotFoundError as err:
                last_err = err

        if last_err is not None:
            raise last_err
        else:
            raise ModuleNotFoundError(module_name)

    def _create_pickler(self, data_buf):
        if self.importers == [importlib.import_module]:
            # if we are using the normal import library system, then
            # we can use the C implementation of pickle which is faster
            return pickle.Pickler(data_buf, protocol=3)
        else:
            return CustomImportPickler(self._import_module, data_buf, protocol=3)

    def save_pickle(self, package: str, resource: str, obj: Any, dependencies: bool = True):
        """Save a python object to the archive using pickle. Equivalent to :func:`torch.save` but saving into
        the archive rather than a stand-alone file. Stanard pickle does not save the code, only the objects.
        If `dependencies` is true, this method will also scan the pickled objects for which modules are required
        to reconstruct them and save the relevant code.

        To be able to save an object where `type(obj).__name__` is `my_module.MyObject`,
        `my_module.MyObject` must resolve to the class of the object according to the `importer` order. When saving objects that
        have previously been packaged, the importer's `import_module` method will need to be present in the `importer` list
        for this to work.

        Args:
            package (str): The name of module package this resource should go it (e.g. "my_package.my_subpackage")
            resource (str): A unique name for the resource, used to indentify it to load.
            obj (Any): The object to save, must be picklable.
            dependencies (bool, optional): If True, we scan the source for dependencies (see :ref:`Dependencies`).
        """
        filename = self._filename(package, resource)
        # Write the pickle data for `obj`
        data_buf = io.BytesIO()
        pickler = self._create_pickler(data_buf)
        pickler.persistent_id = self._persistent_id
        pickler.dump(obj)
        data_value = data_buf.getvalue()

        if dependencies:
            all_dependencies = []
            for opcode, arg, pos in pickletools.genops(data_value):
                if opcode.name == 'GLOBAL':  # a global reference
                    assert isinstance(arg, str)
                    module, field = arg.split(' ')
                    if module not in all_dependencies:
                        all_dependencies.append(module)

            for dep in all_dependencies:
                self.debug_deps.append((package + '.' + resource, dep))

            if self.verbose:
                dep_string = ''.join(f'  {dep}\n' for dep in all_dependencies)
                print(f"{resource} depends on:\n{dep_string}\n")

            for module_name in all_dependencies:
                self.require_module_if_not_provided(module_name)

        self._write(filename, data_value)

    def save_text(self, package: str, resource: str, text: str):
        """Save text data to the package

        Args:
            package (str): The name of module package this resource should go it (e.g. "my_package.my_subpackage")
            resource (str): A unique name for the resource, used to indentify it to load.
            text (str): The contents to save
        """
        return self.save_binary(package, resource, text.encode('utf-8'))

    def save_binary(self, package, resource, binary: bytes):
        """Save raw bytes to the package.

        Args:
            package (str): The name of module package this resource should go it (e.g. "my_package.my_subpackage")
            resource (str): A unique name for the resource, used to indentify it to load.
            binary (str): The data to save.
        """
        filename = self._filename(package, resource)
        self._write(filename, binary)

    def extern_module(self, module_name: str):
        """Include `module` in the list of external modules the package can import.
        This will prevent dependency discover from saving
        it in the package. The importer will load an external module directly from the standard import system.
        Code for extern modules must also exist in the process loading the package.

        Args:
            module_name (str): e.g. "my_package.my_subpackage" the name of the external module
        """
        if module_name not in self.external:
            self.external.append(module_name)

    def extern_modules(self, module_names: List[str]):
        """Extern a list of modules. Convience wrapper for calling :meth:`extern_module` on many items.

        Args:
            module_names (List[str]): List of module names
        """
        for m in module_names:
            self.extern_module(m)

    def mock_module(self, module_name: str):
        """Replace the code for `module_name` in the package with a fake implementation. This module will return a fake
        object for any attribute accessed from it. Because we copy file-by-file, the dependency resolution will sometimes
        find files that are imported by model files but whose functionality is never used
        (e.g. custom serialization code or training helpers).
        Use this function to mock this functionality out without having to modify the original code.

        Args:
            module_name (str): e.g. "my_package.my_subpackage" the name of the module to be mocked out.
        """
        if '_mock' not in self.provided:
            self.save_source_file('_mock', str(Path(__file__).parent / '_mock.py'), dependencies=False)
        is_package = hasattr(self._import_module(module_name), '__path__')
        self.save_source_string(module_name, _MOCK_IMPL, is_package, dependencies=False)


    def mock_modules(self, module_names):
        """Mock a list of modules. Convience wrapper for calling :meth:`mock_module` on many items.

        Args:
            module_names (List[str]): List of module names
        """
        for module_name in module_names:
            self.mock_module(module_name)

    def _module_is_already_provided(self, qualified_name: str) -> bool:
        for mod in self.external:
            if qualified_name == mod or qualified_name.startswith(mod + '.'):
                return True
        return qualified_name in self.provided

    def _persistent_id(self, obj):
        # FIXME: the docs say that persistent_id should only return a string
        # but torch store returns tuples. This works only in the binary protocol
        # see
        # https://docs.python.org/2/library/pickle.html#pickling-and-unpickling-external-objects
        # https://github.com/python/cpython/blob/master/Lib/pickle.py#L527-L537
        if torch.is_storage(obj):
            storage_type = normalize_storage_type(type(obj))
            obj_key = str(obj._cdata)
            location = location_tag(obj)
            self.serialized_storages[obj_key] = obj

            return ('storage',
                    storage_type,
                    obj_key,
                    location,
                    obj.size())
        return None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def _write(self, filename, str_or_bytes):
        if isinstance(str_or_bytes, str):
            str_or_bytes = str_or_bytes.encode('utf-8')
        self.zip_file.write_record(filename, str_or_bytes, len(str_or_bytes))

    def close(self):
        """Write the package to the filesystem. Any calls after close are now invalid.
        It is preferable to use resource guard syntax instead:

            with PackageExporter("file.zip") as e:
                ...
        """
        if self.verbose:
            print(f"Dependency graph for exported package: {self._write_dep_graph()}")

        # Write each tensor to a file named tensor/the_tensor_key in the zip archive
        for key in sorted(self.serialized_storages.keys()):
            name = 'data/{}'.format(key)
            storage = self.serialized_storages[key]
            if storage.device.type == 'cpu':
                # If it's on the CPU we can directly copy it into the zip file
                num_bytes = storage.size() * storage.element_size()
                self.zip_file.write_record(name, storage.data_ptr(), num_bytes)
            else:
                # Copy to a buffer, then serialize that
                buf = io.BytesIO()
                storage._write_file(buf, _should_read_directly(buf))
                buf_value = buf.getvalue()
                self._write(name, buf_value)
        contents = ('\n'.join(self.external) + '\n')
        self._write('extern_modules', contents)
        del self.zip_file


    def _filename(self, package, resource):
        package_path = package.replace('.', '/')
        resource = _normalize_path(resource)
        return f'{package_path}/{resource}'

    def _can_implicitly_extern(self, module_name: str):
        return module_name == 'torch' or (module_name not in _DISALLOWED_MODULES
                                          and _is_builtin_or_stdlib_module(self._import_module(module_name)))


# even though these are in the standard library, we do not allow them to be
# automatically externed since they offer a lot of system level access
_DISALLOWED_MODULES = ['sys', 'io']

def _is_builtin_or_stdlib_module(module: types.ModuleType) -> bool:
    if module.__name__ in sys.builtin_module_names:
        return True
    filename = getattr(module, '__file__', None)
    if filename is None:
        return False
    standard_lib = get_python_lib(standard_lib=True)
    # this is often a subdirectory of standard_lib so we have to check
    # that the file is in the standard_lib directory but not in this one
    installed_libs = get_python_lib(standard_lib=False)
    in_standard_lib = filename.startswith(standard_lib + '/')
    in_installed_libs = filename.startswith(installed_libs + '/')
    return in_standard_lib and not in_installed_libs

_MOCK_IMPL = """\
from _mock import MockedObject
def __getattr__(attr: str):
    return MockedObject(__name__ + '.' + attr)
"""

def _read_file(filename: str) -> str:
    with open(filename, 'rb') as f:
        b = f.read()
        return b.decode('utf-8')
