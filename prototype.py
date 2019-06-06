"""
原型模式：
使用原型实例指定这些对象的创建种类，并通过克隆这些原型创建新对象

适用场景：
对象的创建过程成本较大时，通过复制创建一个相似的对象

扩展阅读：
浅克隆和深克隆
"""


class ProtoType:
    value = 'default'

    def clone(self, **attr):
        obj = self.__class__()
        obj.__dict__ = self.__dict__
        obj.__dict__.update(**attr)
        return obj


if __name__ == "__main__":
    a = ProtoType()
    b = a.clone(value='bbb')
    print(b.value)