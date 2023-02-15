"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib

from setuptools import find_packages, setup

PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()

long_description = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")

setup(
    name="tflite-metadata",
    version="0.0.1",
    description="Provides the compiled python files from the tflite support repository.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["builder*"]),
    python_requires=">=3.10, <4",
    # only functional dependencies, no dev dependencies (like pytest)
    install_requires=[],
    extras_require={
        "dev": ["build"],
        "test": ["pytest"],
        "build": ["click", "requests"],
    },
)
