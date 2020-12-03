import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastpipeline", # Replace with your own username
    version="0.0.2",
    author="Shashank Yadav",
    author_email="shashank7.iitd@gmail.com",
    description="Build time saving ML pipelines with built in autosave and reload",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shashank-yadav/fastpipeline",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.4',
)