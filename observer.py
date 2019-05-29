"""
观察者模式：
被观察者维护一个观察者列表，有任何变化的时候，通知观察者

应用：
django signals：Django Signals: https://docs.djangoproject.com/en/2.1/topics/signals/
"""

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, ob):
        self._observers.append(ob)

    def dettach(self, ob):
        try:
            self._observers.remove(ob)
        except ValueError:
            pass

    def notify(self):
        for ob in self._observers:
            # 观察者必须要实现update方法
            ob.update(self)


class Data(Subject):
    def __init__(self):
        self._data = 0
        super().__init__()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class FirstOb:
    def update(self, subject):
        print('first observer received Subject data: {}'.format(subject.data))


class SecondOb:
    def update(self, subject):
        print('second observer received Subject data: {}'.format(subject.data))


if __name__ == "__main__":
    data = Data()
    fi = FirstOb()
    se = SecondOb()
    data.attach(fi)
    data.attach(se)
    print('alter data subject data')
    data.data = 2
