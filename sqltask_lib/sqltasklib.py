import os
from pathlib import Path


class Template(object):
    def __init__(self, library_root, relative_path):
        self.library_root = library_root
        self.relative_path = relative_path
        self.reader = None

    def name(self):
        return self.relative_path.name

    def relative_path_to_lib(self):
        return self.library_root / self.relative_path

    def testpath(self):
        parts = list(self.relative_path_to_lib().parts)
        parts[parts.index("templates")] = "test_templates"
        parts[-1] = "test_" + parts[-1]  # replace filename
        return Path(*parts)

    def short_description(self):
        reader = self.reader
        result = ""
        for line in self._text_reader():
            result += line
        reader.close()
        return result

    def _text_reader(self):
        if not self.reader:
            reader = open(self.relative_path_to_lib(), "r")
        return reader


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
        # return [
        #     EntitySection("Agent"),
        #     EntitySection("Entity Definition"),
        #     EntitySection("Uncategorized"),
        # ]
