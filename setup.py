from glob import glob
from os.path import basename
from os.path import splitext

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intervalsicu",
    version="0.1.1",
    author="Ryan Day",
    author_email="ryanday2@gmail.com",
    description="A basic interface to the Intervals.icu system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rday/py-intervalsicu",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    python_requires=">=3.6",
    install_requires=["requests==2.25.1", "pytest==6.2.2"]
)
