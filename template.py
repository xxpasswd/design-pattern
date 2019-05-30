"""
模板方法：
定义一个算法的基本框架，而将一些步骤延迟到子类中

优点：
1. 定义好算法得到执行步骤，子类去具体化每个步骤的实现，不会影响算法的执行步骤
2. 将公共行为放到父类中，提高了代码的复用率

应用场景：
需要流程化执行的地方，但具体的每个流程有所变化
"""

def template_fun(eat, work):
    print('every time, first I eat some fund, then start working')
    eat()
    work()


def eat_apple():
    print('eat an apple')


def eat_balana():
    print('eat a balana')


def clean_room():
    print('clean room')


def study():
    print('study')


if __name__ == "__main__":
    template_fun(eat_apple, clean_room)
    template_fun(eat_balana, study)