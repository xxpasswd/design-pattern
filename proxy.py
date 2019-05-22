"""
代理模式：
给某个对象提供一个代理，并由代理对象控制原对象的访问

应用场景：
1. 远程代理，将远程的调用代理给本地的一个对象
2. 虚拟代理，当需要创建一个资源消耗比较大的对象时，可以给它一个资源消耗较小的代理对象，当真正
需要资源的时候，再去访问原对象
3. 保护代理，控制一个对象的访问
4. 缓冲代理
"""

class SalesManager:
    def talk(self):
        print('Sales Manager ready to talk')


class ProxySale:
    def __init__(self):
        self.busy = False
        self.sales = None

    def talk(self):
        if not self.busy:
            self.sales = SalesManager()
            self.sales.talk()
        else:
            print('Sales Manager is busy')


class NoTalkProxySale(ProxySale):
    def talk(self):
        print('I am not tell sales manager, so he is not talk to you')


if __name__ == "__main__":
    p = ProxySale()
    p.talk()
    p.busy = True
    p.talk()

    p2 = NoTalkProxySale()
    p2.talk()
