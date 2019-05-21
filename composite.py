"""
组合模式：
组合多个对象形成树结构来表示具有“整体----部分”关系的分层结构，组合模式对单个对象和组合对象
的处理具有一致性。

优点：
1. 可以很清楚的定义分层次的复杂对象
2. 客户端可以对层次中的对象使用一致的操作，而不用关心不同的对象

应用场景：
需要树形结构的地方
"""

class File:
    def info(self):
        raise NotImplementedError('you should implement this')


class ImageFile(File):
    def __init__(self, name):
        self.name = name

    def info(self):
        print('it is an image file {}'.format(self.name))


class TextFile(File):
    def __init__(self, name):
        self.name = name

    def info(self):
        print('it is a text file {}'.format(self.name))


class Folder(File):
    def __init__(self, name):
        self.name = name
        self.files = []

    def info(self):
        print('get files in {}'.format(self.name))
        for f in self.files:
            f.info()

    def add(self, f):
        self.files.append(f)

    def remove(self, f):
        self.files.remove(f)


if __name__ == "__main__":
    image1 = ImageFile('iamge1')
    image2 = ImageFile('image2')
    text1 = TextFile('text1')
    text2 = TextFile('text2')

    folder1 = Folder('folder1')
    folder2 = Folder('folder2')

    folder1.add(image1)
    folder1.add(image2)
    folder1.add(text1)
    folder2.add(text2)
    folder2.add(folder1)

    folder2.info()