from sqltask_lib.document import EntitySection, TemplateSection
from sqltask_lib.sqltasklib import SQLTaskLib

from mdutils.mdutils import MdUtils


class DocGenerator(object):
    def __init__(self, rootpath):
        self.rootpath = rootpath

    def generate(self, path):
        mdFile = MdUtils(file_name=str(path), title="SQLTask Library")

        for section in self._sections():
            section.append_to(mdFile)
        mdFile.new_table_of_contents(table_title="Contents", depth=2)
        mdFile.create_md_file()

    def _sections(self):
        result = []
        sections = SQLTaskLib(self.rootpath).sections()
        for section_name, templates in sections.items():
            result.append(self._make_section(section_name, templates))
        return result

    def _make_section(self, name, templates):
        md_section = EntitySection(name)
        for template in templates:
            md_section.append(TemplateSection(template))
        return md_section
