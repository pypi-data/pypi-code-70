'''
Created on 12/02/2020

@author: luisza
'''

from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

README = open(os.path.join(os.path.dirname(__file__), 'Readme.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


version = '0.1.5'

setup(
    author='Luis Zarate Montero',
    author_email='luis.zarate@solvosoft.com',
    name='djgentelella',
    version=version,
    description='Extra widgets for django using gentelella.',
    long_description=README,
    url='https://solvosoft.com',
    license='GNU General Public License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
	    'django-mptt>=0.11.0',
        'django-chunked-upload>=2.0.0',
        'djangoajax>=3.2',
        'django-markitup>=4.0.0',
        'markdown',
        'Pillow'
    ],
    packages=find_packages(exclude=["demo", 'doc']),
    include_package_data=True,
    zip_safe=False
)
