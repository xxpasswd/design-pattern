"""
继续调用下一个对象方法

适用场景：
可以将一系列调用的方法，看为一整体动作

使用案例：
https://github.com/dbader/schedule
"""


class Person:
    def __init__(self, name):
        self.name = name

    def action(self):
        print('{} do action'.format(self.name))
        return Action(self)


class Action:
    def __init__(self, person):
        pass

    def move(self, nums):
        print('move {} steps'.format(nums))
        return self

    def jump(self):
        print('jump jump')
        return self

    def stop(self):
        print('stop!')
        return self


if __name__ == "__main__":
    p = Person('Linda')
    p.action().move(4).jump().stop()
    p.action().jump().move(1).stop()