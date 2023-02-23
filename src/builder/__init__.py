import shutil
import subprocess
from logging import info
from pathlib import Path

import click
import requests
from git import Repo

PROJECT_ROOT = Path(__file__).parents[2]
PACKAGES_ROOT = PROJECT_ROOT / "src"
TFLITE_METADATA_ROOT = PACKAGES_ROOT / "tflite_metadata"
SCHEMA_ROOT = TFLITE_METADATA_ROOT / "schema"
TFLITE_ROOT = PACKAGES_ROOT / "tflite"


def update_schema_from_remote(source_repo, revision, filepath):
    schema_url = f"https://raw.githubusercontent.com/{source_repo}/{revision}/{filepath}"
    info(f"Downloading schema from {source_repo}@{revision}")
    schema = requests.get(schema_url).text
    schema_path = SCHEMA_ROOT / Path(filepath).name
    with open(schema_path, "w", encoding="UTF-8") as file:
        file.write(schema)


def compile_schema(schema_path, target_dir):
    info(f"Compiling {schema_path.stem}")
    subprocess.run(
        ["flatc", "--python", "--gen-object-api", schema_path],
        cwd=target_dir,
        check=True,
    )


def update_flatbuffer_schemata(tflite_support_revision=None, tensorflow_revision=None):
    """
    Updates the flatbuffer schema to the latest version.
    """
    if tflite_support_revision is None:
        tflite_support_revision = "master"
    if tensorflow_revision is None:
        tensorflow_revision = "master"
    update_schema_from_remote(
        source_repo="tensorflow/tflite-support",
        filepath="tensorflow_lite_support/metadata/metadata_schema.fbs",
        revision=tflite_support_revision,
    )
    update_schema_from_remote(
        source_repo="tensorflow/tensorflow",
        filepath="tensorflow/lite/schema/schema.fbs",
        revision=tensorflow_revision,
    )


def are_libs_outdated():
    repo = Repo(PROJECT_ROOT)
    modified_files = [item.a_path for item in repo.index.diff(None)]
    return len(modified_files) > 0


def update_compiled_libs():
    info("Remove old files")
    shutil.rmtree(TFLITE_ROOT)
    info("Compile schemata")
    for schema_file in (f for f in SCHEMA_ROOT.iterdir() if f.suffix == ".fbs"):
        compile_schema(schema_file, PACKAGES_ROOT)
    info("Done")


def compile_schemata():
    if are_libs_outdated():
        update_compiled_libs()
    else:
        info("No upstream changes")


@click.group()
def cli():
    pass


@cli.command("update", help="Updates the python files for the metadata schema.")
@click.option("--tflite_support_revision", "-tfls", type=str)
@click.option("--tensorflow_revision", "-tf", type=str)
def update_cmd(**kwargs):
    update_flatbuffer_schemata(**kwargs)


@cli.command(
    "compile",
    help="Assumes `flatc` to be available on path. See https://google.github.io/flatbuffers/",
)
def compile_cmd():
    compile_schemata()
