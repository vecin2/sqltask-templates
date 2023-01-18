from pathlib import Path

from sqltask_lib.document import EntitySection, TemplateSection

from mdutils.mdutils import MdUtils


class DocGenerator(object):
    def __init__(self, tasklib):
        self.tasklib = tasklib

    def generate(self, path=Path("docs/templates.md")):
        mdFile = MdUtils(file_name=str(path), title="SQLTask Library")
        sections = self._sections()
        self.append_summary(mdFile, sections)
        self.append_table_of_contents(mdFile)
        for section in sections:
            print(f"Generating Section {section.title}")
            section.append_to(mdFile)
        mdFile.new_table_of_contents(
            table_title="Table Of Contents", depth=2, marker="Table Of Contents"
        )
        mdFile.create_md_file()
        print(f"\n{path} has been generated")

    def append_table_of_contents(self, mdFile):
        mdFile.new_header(level=1, title="Table Of Contents")

    def append_summary(self, mdFile, sections):
        counter = 0
        summary = ""
        for section in sections:
            summary += f"{len(section.templates)} {section.anchor()}, "
            counter += len(section.templates)
        summary = f"Currently there is total of {counter} templates, divided in {len(sections)} sections; {summary}"
        mdFile.new_paragraph(summary)

    def _sections(self):
        result = []
        sections = self.tasklib.sections()
        for section_name, templates in sections.items():
            result.append(self._make_section(section_name, templates))
        return result

    def _make_section(self, name, templates):
        md_section = EntitySection(name)
        for template in templates:
            md_section.append(TemplateSection(template))
        return md_section
