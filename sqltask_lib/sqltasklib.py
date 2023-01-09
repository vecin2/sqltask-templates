import os
from pathlib import Path

from sqltask_lib.parser import IniParser, JinjaCommentParser


class TemplateInfo(object):
    def __init__(self, text):
        self.text = text
        self._ini_parser = None

    def short_description(self):
        return self._get_ini_parser().get("short_description")

    def _get_ini_parser(self):
        if not self._ini_parser:
            self._ini_parser = IniParser(self.text)
        return self._ini_parser


class Template(object):
    def __init__(self, library_root, relative_path):
        self.library_root = library_root
        self.relative_path = relative_path
        self.reader = None
        self._info = None

    def info(self):
        if not self._info:
            self._info = TemplateInfo(
                JinjaCommentParser().parse_top_comment(self.content())
            )
        return self._info

    def name(self):
        return self.relative_path.name

    def relpath(self):
        return self.library_root.name / self.relative_path

    def abspath(self):
        return self.library_root / self.relative_path

    def content(self):
        with open(self.abspath()) as file:
            return "".join(file.readlines())
        return ""

    def testpath(self):
        parts = list(self.relpath().parts)
        parts[parts.index("templates")] = "test_templates"
        parts[-1] = "test_" + parts[-1]  # replace filename
        return Path(*parts)

    def short_description(self):
        return self.info().short_description()

    def _reader(self):
        if not self.reader:
            self.reader = open(self.relative_path_to_lib(), "r")
        return self.reader


class SQLTaskLib(object):
    def __init__(self, rootpath):
        self.rootpath = rootpath
        self.templates_path = rootpath / "templates"

    def listall(self):
        templates = []
        exclude_set = set(["tutorials"])
        for current_folder, dirs, files in os.walk(self.templates_path):
            # it removes subdirs inline so they are not processed by walk
            dirs[:] = [d for d in dirs if d not in exclude_set]
            for filename in files:
                absolute_filepath = Path(current_folder + "/" + filename)
                relative_path = absolute_filepath.relative_to(self.rootpath)
                templates.append(Template(self.rootpath, relative_path))
        return templates

    def save_template_content(self, template_path, content):
        (self.templates_path / template_path).write_text(content)

    def load_template(self, template_path):
        return Template(self.rootpath, template_path)

    # return [
    #     EntitySection("Agent"),
    #     EntitySection("Entity Definition"),
    #     EntitySection("Uncategorized"),
    # ]
