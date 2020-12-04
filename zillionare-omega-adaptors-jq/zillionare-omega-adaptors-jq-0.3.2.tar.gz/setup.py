#!/usr/bin/env python
"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "arrow~=0.15",
    "ruamel.yaml~=0.16",
    "numpy==1.19.4",
    "jqdatasdk>=1.8",
    "pytz>=2019.3",
    "zillionare-omicron>=0.1",
    "cfg4py>=0.8.0",
    "ruamel.yaml>=0.16",
]

setup_requirements = []

test_requirements = []

setup(
    author="Aaron Yang",
    author_email="code@jieyu.ai",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
    ],
    description="Jqdatasdk adapter for zillionare omega",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="zillionare, omega, adaptors, jqdatasdk",
    name="zillionare-omega-adaptors-jq",
    packages=find_packages(include=["jqadaptor", "jqadaptor.*"]),
    setup_requires=setup_requirements,
    url="https://github.com/zillionare/omega_jqadaptor",
    version="0.3.2",
    zip_safe=False,
)
