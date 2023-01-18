from pathlib import Path

import fire
from sqltask_lib import DocGenerator, Renamer, SQLTaskLib, current_path

TASK_LIBRARY = SQLTaskLib(current_path.absolute("prj_config"))


def generate_docs():
    DocGenerator(TASK_LIBRARY).generate(Path("docs/templates.md"))


def rename(old_name, new_name):
    Renamer(TASK_LIBRARY).rename(old_name, new_name)


if __name__ == "__main__":
    fire.Fire({"generate_docs": generate_docs, "rename": rename})
