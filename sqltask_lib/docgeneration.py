from mdutils.mdutils import MdUtils
from sqltask_lib.document import EntitySection, TemplateSection
from sqltask_lib.sqltasklib import SQLTaskLib


class DocGenerator(object):
    def __init__(self, rootpath):
        self.rootpath = rootpath

    def generate(self, path):
        mdFile = MdUtils(file_name=str(path), title="Markdown File Example")

        for entity in self.entities():
            entity.append_to(mdFile)

        mdFile.create_md_file()

    def entities(self):
        section = EntitySection("Uncategorized")
        templates = SQLTaskLib(self.rootpath).listall()
        for template in templates:
            section.append(TemplateSection(template))
        return [section]
