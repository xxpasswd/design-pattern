"""
单例模式：
确保只要一个类实例能够创建

为什么要使用单例模式？
有些时候，我们需要确保一个对象只能创建一次，在全局中使用的时候都是同一个对象，比如我们有一个全局控状态记
录类，里面有很多属性记录着全局的状态，当我们实例化的时候，我就希望只有一个全局记录对象，所有的状态变化都记录
在这个对象里面；如果说有多个这样的全局记录对象，我们就很难记录全局的状态，到底要更新哪个全局记录对象，哪个的
记录数据是正确的。

应用场景：
(1) 系统只需要一个实例对象，比如资源管理器，唯一序号生产器，或者考虑资源消耗太大，只允许创建一个对象
(2) 只允许使用一个公共的访问点，比如数据库连接，日志

参考资料：
(1) https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
(2)《设计模式的艺术》

扩展阅读：
饿汉单例模式，懒汉单例模式
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