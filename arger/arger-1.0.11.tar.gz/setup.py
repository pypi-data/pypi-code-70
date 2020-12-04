# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arger']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'arger',
    'version': '1.0.11',
    'description': 'Create argparser automatically from functions',
    'long_description': '# Overview\n\nA wrapper around argparser to help build CLIs from functions. Uses type-hints extensively :snake:.\n\n[![PyPi Version](https://img.shields.io/pypi/v/arger.svg?style=flat)](https://pypi.python.org/pypi/arger)\n[![Python Version](https://img.shields.io/pypi/pyversions/arger.svg)](https://pypi.org/project/arger/)\n![](https://github.com/jnoortheen/arger/workflows/test-and-publish/badge.svg)\n![](https://github.com/jnoortheen/arger/workflows/codeql-analysis/badge.svg)\n![](https://img.shields.io/badge/dynamic/json?label=coverage&query=%24.coverage.status&url=https%3A%2F%2Fraw.githubusercontent.com%2Fjnoortheen%2Farger%2Fshields%2Fshields.json)\n[![PyPI License](https://img.shields.io/pypi/l/arger.svg)](https://pypi.org/project/arger)\n\n# Setup\n\n## :gear: Installation\n\nInstall it directly into an activated virtual environment:\n\n``` text\n$ pip install arger\n```\n\nor add it to your [Poetry](https://poetry.eustace.io/) project:\n\n``` text\n$ poetry add arger\n```\n\n# :books: Usage\n\n* create a python file called test.py\n\n``` python\nfrom arger import Arger\n\ndef main(param1: int, param2: str, kw1=None, kw2=False):\n    """Example function with types documented in the docstring.\n\n    :param param1: The first parameter.\n    :param param2: The second parameter.\n    """\n    print(locals())\n\nif __name__ == \'__main__\':\n    Arger(main).run()\n```\n\n* Here Arger is just a subclass of `ArgumentParser`. It will not conceal you from using other `argparse` libraries.\n\n* run this normally with\n\n``` sh\npython test.py 100 param2\n```\n\n* Checkout [examples](docs/examples) folder and documentation to see more of `arger` in action. It supports any level of sub-commands.\n\n# Features\n\n- Uses docstring to parse help comment for arguments. Supports\n    + [google](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)\n    + [numpy](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy)\n    + [rst](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)\n- Flags will be generated from parameter-name. \n  If needed you could declare it inside docstring like `:param arg1: -a --arg this is the document`.\n  Also one can use `def main(arg1:int=Option(\'-a\', \'--arg\')): ...`\n- The decorated functions can be composed to form nested sub-commands of any level.\n- No external lib dependency\n- Most of the Standard types [supported](./tests/test_args_opts/test_arguments.py). \n  Please see [examples](./docs/examples/4-supported-types/src.py) for more supported types with examples.\n- All argument to `ArgumentParser.add_argument` is supported. \n  It can be updated with `arger.Argument` or `arger.Option` classes.\n- `*args` supported but no `**kwargs` support yet.\n- all optional arguments that start with underscore is not passed to `Parser`. \n  They are considered private to the function implementation.\n  One can use `_namespace_` to get the output from the `ArgumentParser.parse_args()`\n  \n\n# Similar Projects\n\n## [argh](https://argh.readthedocs.io/en/latest/tutorial.html)\n\n - has similar goals as to ease up using argparser.\n - doesn\'t support type hints.\n - No recent releases.\n\n## [typer](https://github.com/tiangolo/typer)\n\n - if you are using `click` , I highly recommend you to check this library.\n - it is neat and many features are drawn from it.\n - doesn\'t support loading help text for arguments from docstrings.\n\n## [invoke](http://www.pyinvoke.org/)\n\n - doesn\'t support type hints.\n\n## [cliche](https://github.com/kootenpv/cliche)\n\n - has similar goals.\n - doesn\'t cover much use cases as `arger` .\n\n## [cliar](https://moigagoo.github.io/cliar/)\n\n - no docstring support for help argument.\n\n# Recommended Alternatives\n\nProjects that I highly recommend you to checkout.\n\n1.  [clize](https://github.com/epsy/clize)\n2.  [nuclear](https://github.com/igrek51/nuclear)\n3.  [defopt](https://github.com/anntzer/defopt)\n\nThis project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter) using [jacebrowning/template-python](https://github.com/jacebrowning/template-python).\n\n\n# Argparser enhancements\n\n* web-ui : https://github.com/nirizr/argparseweb\n* extra actions : https://github.com/kadimisetty/action-hero\n* automatic shell completions using [argcomplete](https://github.com/kislyuk/argcomplete)\n\n',
    'author': 'Noortheen Raja',
    'author_email': 'jnoortheen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/arger',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
