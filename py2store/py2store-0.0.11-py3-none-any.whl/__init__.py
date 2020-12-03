import os
from py2store.util import ModuleNotFoundIgnore

file_sep = os.path.sep


def kvhead(store, n=1):
    """Get the first item of a kv store, or a list of the first n items"""
    if n == 1:
        for k in store:
            return k, store[k]
    else:
        return [(k, store[k]) for i, k in enumerate(store) if i < n]


def ihead(store, n=1):
    """Get the first item of an iterable, or a list of the first n items"""
    if n == 1:
        for item in iter(store):
            return item
    else:
        return [item for i, item in enumerate(store) if i < n]


from py2store.util import (
    lazyprop,
    partialclass,
    groupby,
    regroupby,
    igroupby
)

from py2store.base import (
    Collection,
    KvReader,
    KvPersister,
    Reader,
    Persister,
    kv_walk,
    Store,
)

from py2store.persisters.local_files import FileReader

from py2store.stores.local_store import (
    LocalStore,
    LocalBinaryStore,
    LocalTextStore,
    LocalPickleStore,
    LocalJsonStore,
    PickleStore,  # consider deprecating and use LocalPickleStore instead?
)
from py2store.stores.local_store import (
    QuickStore,
    QuickBinaryStore,
    QuickTextStore,
    QuickJsonStore,
    QuickPickleStore,
)
from py2store.stores.local_store import (
    DirReader,
    DirStore,
)

from py2store.misc import (
    MiscGetter,
    MiscGetterAndSetter,
    misc_objs,
    misc_objs_get,
    get_obj,
    set_obj,
)

from py2store.trans import (
    wrap_kvs,
    disable_delitem,
    disable_setitem,
    mk_read_only,
    kv_wrap,
    cached_keys,
    filt_iter,
    filtered_iter,
    add_path_get,
    insert_aliases,
    add_ipython_key_completions,
    cache_iter,  # being deprecated
)
from py2store.access import (
    user_configs_dict,
    user_configs,
    user_defaults_dict,
    user_defaults,
)
from py2store.caching import (
    mk_cached_store,
    store_cached,
    store_cached_with_single_key,
    ensure_clear_to_kv_store,
    flush_on_exit,
    mk_write_cached_store,
)

from py2store.appendable import (
    appendable
)

from py2store.slib.s_zipfile import (
    ZipReader,
    ZipFilesReader,
    FilesOfZip,
    FlatZipFilesReader,
)

from py2store.key_mappers.naming import StrTupleDict
from py2store.key_mappers.paths import mk_relative_path_store

###### Optionals... ##############################################################################

with ModuleNotFoundIgnore():
    from py2store.access import myconfigs
with ModuleNotFoundIgnore():
    from py2store.access import mystores

with ModuleNotFoundIgnore():
    from py2store.stores.s3_store import (
        S3BinaryStore,
        S3TextStore,
        S3PickleStore,
    )
with ModuleNotFoundIgnore():
    from py2store.stores.mongo_store import (
        MongoStore,
        MongoTupleKeyStore,
        MongoAnyKeyStore,
    )
