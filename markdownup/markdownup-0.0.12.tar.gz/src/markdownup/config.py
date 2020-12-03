from copy import deepcopy

default_config = {
    'main': {
        'theme': 'default'
    },
    'wsgi': {
        'bind': '127.0.0.1:8080',
        'workers': 1
    },
    'content': {
        'indices': [
            'README.md',
            'index.md'
        ],
        'gits': {}
    },
    'markdown': {
        'extensions': [
            'extra',
            'codehilite'
        ]
    },
    'access': {
        r'.*/\.': False,  # nobody has access to hidden files and directories
        r'.*': True  # everybody has access to everything else
    }
}


def extend_default_config(extension):
    config = deepcopy(default_config)
    for group, values in extension.items():
        for key, value in values.items():
            config[group][key] = value
    return config
