# coding: utf-8

"""
    Chino.Scriba API

    Audit log management API  # noqa: E501

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Modified by Stefano to accomodate readme (2020.01.09)
"""

from setuptools import setup, find_packages  # noqa: H301
from os import path


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
NAME = "chinoscriba"
VERSION = "0.0.0.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Chino.io Scriba SDK Python",
    author_email="",
    url="https://www.chino.io",
    keywords=["Chino.io Scriba API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
	long_description_content_type="text/markdown",
	long_description=long_description,
    # classifiers=[
    #     "Topic :: Software Development",
    # "Development Status :: 5 - Production/Stable",
    # "Programming Language :: Python :: 2",
    # "Programming Language :: Python :: 3"]
    )