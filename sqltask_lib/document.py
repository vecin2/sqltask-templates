class StringBuilder(object):
    def __init__(self):
        self.segments = []

    def append(self, text):
        self.segments.append(text)
        return self

    def append_line(self, text):
        if self.segments:
            self.append("\\").append("\n")
        self.append(text)

    def build(self):
        return "".join(self.segments)


class RenderableNode(object):
    def __init__(self, renderableNode=None):
        self.sb = StringBuilder()
        self.nodes = []
        if renderableNode:
            self.nodes.append(renderableNode)

    def append(self, node):
        self.nodes.append(node)
        return self

    def render(self, save_location):
        for node in self.nodes:
            self.sb.append(node.render(save_location))
        return self.sb.build()


class TextNode(object):
    def __init__(self, text):
        self.text = text

    def render(self, save_location):
        return self.text


class HeaderNode(object):
    def __init__(self, text, level):
        self.text = text
        self.level = level

    def render(self, save_location):
        return (self.level * "#") + " " + self.text + "\n"


class MarkdownDoc(RenderableNode):
    def __init__(self, title):
        super().__init__()
        self.with_title(title)
        self.text = ""

    def with_title(self, title):
        self.nodes.append(HeaderNode(title, level=1))
        return self

    def save(self, path):
        path.write_text(self.render(path))


class MarkdownRelativeLink(object):
    def __init__(self, name, url_to):
        self.name = name
        self.url_to = url_to

    def render(self, save_location):
        return f"[{self.name}]({self._get_url(save_location)})"

    def _get_url(self, save_location):
        result = ""

        for parent in save_location.parents:
            result = ".." / parent
        return result / self.url_to


class LineNode(RenderableNode):
    def __init__(self, renderableNode):
        super().__init__(renderableNode)

    def render(self, save_location):
        result = super().render(save_location)
        if result:
            return result + "\\" + "\n"
        return result


class EntitySection(RenderableNode):
    def __init__(self, title):
        self.nodes = []
        self.with_title(title)
        self.sb = StringBuilder()

    def with_title(self, title):
        self.nodes.append(HeaderNode(title, level=2))
        return self


class BreakLineNode(object):
    def render(self, save_location):
        return "<br>" + "\n"


class TemplateSection(RenderableNode):
    def __init__(self, template):
        super().__init__()
        self.template = template
        self.template_link = MarkdownRelativeLink(
            self.template.name(), self.template.relpath()
        )
        testpath = self.template.testpath()
        self.test_link = MarkdownRelativeLink(testpath.name, testpath)

    def append_to(self, renderableNode):
        renderableNode.append(HeaderNode(self.template.name(), level=3))
        renderableNode.append(TextNode(self.template.short_description()))
        renderableNode.append(TextNode("Template: "))
        renderableNode.append(self.template_link).append(BreakLineNode())
        renderableNode.append(TextNode("Test: "))
        renderableNode.append(self.test_link).append(BreakLineNode())


class MarkdownTemplate(RenderableNode):
    def __init__(self, template):
        super().__init__()
        link = MarkdownRelativeLink(template.name(), template.relative_path_to_lib())
        self.nodes.append(LineNode(link))

        self.template = template
