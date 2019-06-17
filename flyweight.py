"""
享元模式：
运用共享技术有效的支持大量细粒度对象的复用。

优点：
大量节省对内存的使用

适用场景：
消耗内存大的地方
"""


class FileFlyWeight:
    pools = {}

    def __new__(cls, name):
        if name not in cls.pools:
            instance = super().__new__(cls)
            cls.pools[name] = instance
        return cls.pools[name]


if __name__ == "__main__":
    image = FileFlyWeight('iamge')
    image2 = FileFlyWeight('iamge')
    print(image == image2)

    text1 = FileFlyWeight('text')
    text2 = FileFlyWeight('text')
    print(text1 == text2)