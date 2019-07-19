"""
备忘录模式：
在不破坏封装的前提下，捕获一个对象的内部状态表示，并在该对象之外保存这个状态，这样可以将
对象恢复到之前的状态

优点：
提供了一种状态恢复的机制

应用场景：
需要保存一个对象的历史状态，以便后面使用
"""


from copy import copy


def memento(obj):
    state = copy(obj.__dict__)
    
    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore


class Transaction:
    states = []
    def __init__(self, obj):
        self.obj = obj
        self.commit()

    def commit(self):
        self.states = [memento(self.obj)]

    def rollback(self):
        for r_state in self.states:
            r_state()


class Transactional:
    """属性描述符"""
    def __init__(self, method):
        self.method = method

    def __get__(self, obj, T):
        def transaction(*arg, **kwargs):
            state = memento(obj)
            try:
                return self.method(obj, *arg, **kwargs)
            except Exception as e:
                state()
                raise e
        return transaction


class NumObj:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def increment(self):
        self.value += 1

    @Transactional
    def do_stuff(self):
        self.value = '111'
        self.increment()


if __name__ == "__main__":
    n = NumObj(1)
    print(n)
    transaction = Transaction(n)
    n.increment()
    print(n)
    n.increment()
    print(n)
    transaction.commit()
    print('commit -- ')
    n.increment()
    print(n)
    n.increment()
    print(n)
    transaction.rollback()
    print('rollback --')
    print(n)

    print('do no stuff...')
    print(n)
    try:
        n.do_stuff()
    except:
        print('exception --')
        import sys
        import traceback
        traceback.print_exc(file=sys.stdout)
        print(n)
