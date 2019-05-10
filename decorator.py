"""
装饰器模式：
给一个对象添加一个新功能，而不需要修改这个对象
"""

class TextTag:
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


class BoldWrapper:
    def __init__(self, text_tag):
        self.wrapper = text_tag

    def render(self):
        return "<b> {} </b>".format(self.wrapper.render())


class ItalicWrapper:
    def __init__(self, text_tag):
        self.wrapper = text_tag

    def render(self):
        return "<i> {} </i>".format(self.wrapper.render())


if __name__ == "__main__":
    simple_str = TextTag('hello')
    bold_str = BoldWrapper(simple_str)
    italic_str = ItalicWrapper(bold_str)
    print(italic_str.render())