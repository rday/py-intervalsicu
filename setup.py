import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intervalsicu",
    version="0.1.0",
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
    python_requires=">=3.6",
)

