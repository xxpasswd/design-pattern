"""
简单工厂模式：
定义一个工厂类，可以根据参数的不同，返回不同的类实例

为什么要使用简单工厂模式？
工厂模式主要是为了解决简单对象的创建问题，将对象的创建和使用分离开来

应用场景：
需要通过传入不同的参数来创建不同的对象
"""
class Dog:
    def who(self):
        print('dog')


class Cat:
    def who(self):
        print('cat')


class Pig:
    def who(self):
        print('pig')


def get_instance(animal):
    """
    简单工厂
    """
    if animal == 'dog':
        return Dog()
    elif animal == 'cat':
        return Cat()
    elif animal == 'pig':
        return Pig()


class Nest:
    """
    这样将nest和animal的创建分离了开来
    更换dog，cat，pig的时候就不需要修改Nest类
    """
    def __init__(self, animal):
        self.animal = get_instance(animal)

    def get_animal(self):
        self.animal.who()


if __name__ == "__main__":
    dog_nest = Nest('dog')
    dog_nest.get_animal()