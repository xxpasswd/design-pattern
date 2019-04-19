"""
单例模式：
确保只要一个类实例能够创建

应用：数据连接，日志，文件管理

参考文档：https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
"""

# 方式一，通过装饰器实现
def singleton(class_)
    instance = {}
    def get_instance(*args, **kwargs):
        if class_ not in instance:
            instance[class_] = class_(*args, **kwargs)
        return instance[class_]
    return get_instance


@singleton
class Myclass:
    pass


# 方法二，使用__new__方法
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Myclass(Singleton):
    pass


# 方法三，使用metaclass
class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class Myclass(metaclass=Singleton):
    pass


# 方法四，共享属性
class Singleton:
    __shared_state = {}
    def __init__(self, *args, **kwargs):
        self.__dict__ = self.__shared_state


class Myclass(Singleton):
    pass


# 方法五，全局导入
class Singleton:
    pass

singleton = Singleton()
# 在其他文件中导入 singleton
from . import singleton