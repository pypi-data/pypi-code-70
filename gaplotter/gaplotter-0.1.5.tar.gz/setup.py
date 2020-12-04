import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gaplotter",
    version="0.1.005",
    author="Gaetan Desrues",
    author_email="gaetan.desrues@inria.fr",
    description="Description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.inria.fr/gdesrues1/plotter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
