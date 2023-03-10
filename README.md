# tflite metadata

This repository provides the compiled python files
from the tflite support repository.
This makes them available for all current python versions on all platforms.

## Setup

### Getting started

1. Make virtual environment and activate it
1. `pip install -e` to install project in the virtual environment
1. `pre_commit install` to install pre-commit hooks (see below)

### Project Setup

Only the contents of the [`builder`](src/builder/__init__.py) package
and the [`tflite_metadata/__init__.py`](src/tflite_metadata/__init__.py) are maintained in this repository.
The rest is autogenerated based of the schemata.

## Tools

### [pre-commit](https://pre-commit.com)

We use pre-commit
to trigger a broad array of actions through git commands.
Code formatting, linting and more can be automated
to run before checking code in.
This increases code and repository quality
(especially in shared projects).
Should these not be installed automatically on your system,
you can run `make pre_commit`.

______________________________________________________________________

### Semantic Line Breaks

This project uses [semantic line breaks](https://sembr.org/) - and you probably should, too.
