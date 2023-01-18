from sqltask_lib.docgeneration import DocGenerator
from sqltask_lib.project_path import ProjectPath
from sqltask_lib.rename import Renamer
from sqltask_lib.sqltasklib import SQLTaskLib

PROJECT_NAME = "sqltask-templates"

current_path = ProjectPath(PROJECT_NAME)

__all__ = ["DocGenerator", "Renamer", "SQLTaskLib"]
