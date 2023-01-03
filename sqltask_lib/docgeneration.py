from sqltask_lib.document import EntitySection, MarkdownDoc, TemplateSection
from sqltask_lib.sqltasklib import SQLTaskLib


class DocGenerator(object):
    def __init__(self, rootpath):
        self.rootpath = rootpath

    def generate(self, path):
        doc = MarkdownDoc("Templates")
        for entity in self.entities():
            doc.append(entity)
        doc.save(path)

    def entities(self):
        section = EntitySection("Uncategorized")
        templates = SQLTaskLib(self.rootpath).listall()
        for template in templates:
            TemplateSection(template).append_to(section)
            # section.append(template)
        return [section]
