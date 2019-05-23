"""
职责链模式：
避免将请求发送者和接收者耦合在一起，让多个对象都有机会接受请求，将这些对象连接成一条链，
在链上依次传递请求，直到有对象处理请求为止。
责任链模式是面向对象版本的if...elif...elif...else... 好处是可以动态的安排条件对象

应用场景：
1. 有多个对象可以处理同一个请求，具体哪一个对象待运行时候再确定
2. 在不明接受者的情况下，向多个对象中的一个发送请求
"""


import abc


class Handler(metaclass=abc.ABCMeta):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        """
        对请求进行判断，并处理
        """
        res = self.check_range(request)
        if not res and self.successor:
            self.successor.handle_request(request)

    @abc.abstractmethod
    def check_range(self, request):
        """
        对请求进行判断，并返回判断结果
        """


class ConcreteHandler(Handler):
    def check_range(self, request):
        if 0 <= request < 10:
            print('process request {} between 0 - 10'.format(request))
            return True


class ConcreteHandler2(Handler):
    def check_range(self, request):
        if 10 <= request < 20:
            print('process request {} between 10 - 20'.format(request))
            return True


class FallbackHandler(Handler):
    def check_range(self, request):
        print('no handle can process this request {}, this is end'.format(request))
        return False


if __name__ == "__main__":
    h1 = ConcreteHandler()
    h2 = ConcreteHandler2(FallbackHandler())

    h1.successor = h2

    requests = [2,7, 11, 23, 15]

    for request in requests:
        h1.handle_request(request)
