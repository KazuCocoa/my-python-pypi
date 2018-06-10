import setuptools

with open("README.md", "r") as fh:
     long_description = fh.read()

setuptools.setup(
    name="my-python-pipy",
    version="0.0.1",
    author="kazucocoa",
    author_email="fly.49.89.over@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/example-project",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
