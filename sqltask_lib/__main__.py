from pathlib import Path

import fire
from sqltask_lib.docgeneration import DocGenerator


class ProjectPath(object):
    def __init__(self, project_name):
        self.project_name = project_name

    def absolute(self, project_relative_path):
        parent_folder = Path(__file__).parent  # parent folder of current file
        current = parent_folder
        while str(current) != str(current.root) and current.name != PROJECT_NAME:
            current = current.parent

        if current.name == PROJECT_NAME:
            return current / project_relative_path
        else:
            raise ValueError(
                f"Project name is set to {PROJECT_NAME}, but no parent folders with that name where found on the current stored location {parent_folder}"
            )


PROJECT_NAME = "sqltask-templates"
project_path = ProjectPath(PROJECT_NAME)
TEMPLATES_PATH = project_path.absolute("prj_config")


def generate_docs():
    filepath = project_path.absolute("docs/templates.md")
    DocGenerator(TEMPLATES_PATH).generate(filepath)


if __name__ == "__main__":
    fire.Fire({"generate_docs": generate_docs})
