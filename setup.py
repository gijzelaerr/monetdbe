import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monetdbe",
    version="0.1",
    author="Gijs Molenaar",
    author_email="gijs@pythonic.nl",
    description="MonetDBe - the Python embedded MonetDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gijzelaerr/monetdbe",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Database :: Front-Ends",
    ],
    python_requires='>=3.5',
    install_requires=[
    ]
)
