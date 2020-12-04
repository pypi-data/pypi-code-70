# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['taobaopyx']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.16.1,<0.17.0']

setup_kwargs = {
    'name': 'taobaopyx',
    'version': '0.1.0',
    'description': 'Asyncio version of taobaopy',
    'long_description': None,
    'author': 'duyixian',
    'author_email': 'duyixian1234@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
