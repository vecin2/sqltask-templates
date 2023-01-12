from pathlib import Path

import fire
from sqltask_lib import current_path
from sqltask_lib.docgeneration import DocGenerator

TASKS_LIBRARY_PATH = current_path.absolute("prj_config")


def generate_docs():
    filepath = current_path.absolute("docs/templates.md")
    DocGenerator(TASKS_LIBRARY_PATH).generate(Path("docs/templates.md"))
    print(f"{filepath} has been generated")


if __name__ == "__main__":
    fire.Fire({"generate_docs": generate_docs})
