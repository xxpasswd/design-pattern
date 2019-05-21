"""
适配器模式
修改一个类的接口变为客户希望的接口，使原本接口不兼容的类能够一起工作

参考文档：https://sourcemaking.com/design_patterns/adapter
"""

class Dog:
    def __init__(self):
        self.name = 'dog'

    def bark(self):
        print('woof')


class Cat:
    def __init__(self):
        self.name = 'cat'

    def meow(self):
        print('meow')


class Human:
    def __init__(self):
        self.name = 'human'

    def hello(self):
        print('hello')


class Adapter:
    """
    usage:

        dog = Dog()
        adapter = Adapter(dog, make_noise=dog.bark)
    """

    def __init__(self, obj, **adpated_method):
        self.obj = obj
        self.__dict__.update(adpated_method)
    
    def __getattr__(self, attr):
        """所有没被适配的方法都会进入这里面"""
        return getattr(self.obj, attr)

if __name__ == '__main__':
    def main():
        objs = []
        dog = Dog()
        objs.append(Adapter(dog, make_noise=dog.bark))
        cat = Cat()
        objs.append(Adapter(cat, make_noise=cat.meow))
        human = Human()
        objs.append(Adapter(human, make_noise=human.hello))

        for o in objs:
            o.make_noise()

    main()