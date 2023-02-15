import logging
import shutil
import subprocess
import tempfile
from logging import info
from pathlib import Path

import click
import requests

PROJECT_ROOT = Path(__file__).parents[2]
PACKAGE_ROOT = PROJECT_ROOT / "src" / "tflite_metadata"


def compile_remote_schema(source_repo, revision, filepath, target_dir):
    schema_url = f"https://raw.githubusercontent.com/{source_repo}/{revision}/{filepath}"
    info(f"Downloading schema from {source_repo}@{revision}")
    schema = requests.get(schema_url).text
    schema_path = Path(target_dir) / Path(filepath).name
    with open(schema_path, "w", encoding="UTF-8") as file:
        file.write(schema)
    info("Compiling schema")
    subprocess.run(
        ["flatc", "--python", "--gen-object-api", schema_path],
        cwd=target_dir,
        check=True,
    )
    schema_path.unlink()


def update_flatbuffer_schema(tflite_support_revision=None, tensorflow_revision=None):
    """
    Updates the flatbuffer schema to the latest version.
    """
    if tflite_support_revision is None:
        tflite_support_revision = "master"
    if tensorflow_revision is None:
        tensorflow_revision = "master"
    with tempfile.TemporaryDirectory() as tmp_dir:
        compile_remote_schema(
            source_repo="tensorflow/tflite-support",
            filepath="tensorflow_lite_support/metadata/metadata_schema.fbs",
            revision=tflite_support_revision,
            target_dir=tmp_dir,
        )
        compile_remote_schema(
            source_repo="tensorflow/tensorflow",
            filepath="tensorflow/lite/schema/schema.fbs",
            revision=tensorflow_revision,
            target_dir=tmp_dir,
        )
        info("Replacing old content")
        package = next(item for item in Path(tmp_dir).iterdir())

        # save non-generated python code
        shutil.move(PACKAGE_ROOT / "__init__.py", package / "__init__.py")

        shutil.rmtree(PACKAGE_ROOT)
        PACKAGE_ROOT.mkdir()
        for module in package.iterdir():
            shutil.move(module, PACKAGE_ROOT)

    info("Done")


@click.command(
    help="Updates the python files for the metadata schema. "
    "Assumes `flatc` to be available on path. "
    "See https://google.github.io/flatbuffers/"
)
@click.option("--tflite_support_revision", "-tfls", type=str)
@click.option("--tensorflow_revision", "-tf", type=str)
def update_flatbuffer_schema_cmd(**kwargs):
    update_flatbuffer_schema(**kwargs)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    update_flatbuffer_schema_cmd()
