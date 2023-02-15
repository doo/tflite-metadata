import shutil
import subprocess
import tempfile
from logging import info
from pathlib import Path

import click
import requests

PROJECT_ROOT = Path(__file__).parents[2]
PACKAGE_ROOT = PROJECT_ROOT / "src" / "tflite_metadata"


def update_flatbuffer_schema(revision=None):
    """
    Updates the flatbuffer schema to the latest version.
    """
    if revision is None:
        revision = "master"
    source_repo = "tensorflow/tflite-support"
    filepath = "tensorflow_lite_support/metadata/metadata_schema.fbs"
    schema_url = f"https://raw.githubusercontent.com/{source_repo}/{revision}/{filepath}"
    info(f"Downloading schema from {source_repo}@{revision}")
    schema = requests.get(schema_url).text
    with tempfile.TemporaryDirectory() as tmp_dir:
        schema_path = Path(tmp_dir) / "schema.fbs"
        with open(schema_path, "w", encoding="UTF-8") as file:
            file.write(schema)
        info("Compiling schema")
        subprocess.run(["flatc", "--python", schema_path], cwd=tmp_dir, check=True)
        info("Replacing old content")
        shutil.rmtree(PACKAGE_ROOT)
        PACKAGE_ROOT.mkdir()
        package = next(item for item in Path(tmp_dir).iterdir() if item != schema_path)
        for module in package.iterdir():
            shutil.move(module, PACKAGE_ROOT)

    info("Done")


@click.command(
    help="Updates the python files for the metadata schema. "
    "Assumes `flatc` to be available on path. "
    "See https://google.github.io/flatbuffers/"
)
@click.option("--revision", "-r", type=str)
def update_flatbuffer_schema_cmd(**kwargs):
    update_flatbuffer_schema(**kwargs)


if __name__ == "__main__":
    update_flatbuffer_schema_cmd()
