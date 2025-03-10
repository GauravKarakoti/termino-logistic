import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

with open(HERE / "setupreq.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="termino",
    version="0.0.0",
    description="cli tool using python to send request to a server",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/debarshee2004/termino-logistic",
    license="Apache",
    entry_points={
        "console_scripts": [
            "termino = app.main:main",
        ],
    },
    python_requires=">=3.12",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
)
