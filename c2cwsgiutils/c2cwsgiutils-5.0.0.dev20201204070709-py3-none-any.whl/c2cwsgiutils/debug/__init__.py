from typing import Optional

import pyramid.config

from c2cwsgiutils import _utils, auth
from c2cwsgiutils.debug import utils

CONFIG_KEY = "c2c.debug_view_enabled"
ENV_KEY = "C2C_DEBUG_VIEW_ENABLED"

# for backward compatibility
get_size = utils.get_size
dump_memory_maps = utils.dump_memory_maps


def init(config: pyramid.config.Configurator) -> None:
    if auth.is_enabled(config, ENV_KEY, CONFIG_KEY):
        from c2cwsgiutils.debug import _views

        init_daemon(config)
        _views.init(config)


def init_daemon(config: Optional[pyramid.config.Configurator] = None) -> None:
    """
    Initialize the debug broadcast listeners. Used mostly for headless processes that depend on a master
    providing a normal REST API and broadcasting those requests.
    """
    if _utils.env_or_config(config, ENV_KEY, CONFIG_KEY, type_=_utils.config_bool):
        from c2cwsgiutils.debug import _listeners

        _listeners.init()
