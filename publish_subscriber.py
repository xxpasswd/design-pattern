"""
发布订阅者模式：
一个订阅者可以订阅多个频道，当发布者更新消息时，会收到相应频道的通知

提供者 ----> 发布者 ----> 订阅者
"""
class Provider:
    def __init__(self):
        self.msg = []
        self.subs = {}

    def put_msg(self, msg):
        self.msg.append(msg)

    def subscribe(self, msg, sub):
        self.subs.setdefault(msg, []).append(sub)

    def unsubscribe(self, msg, sub):
        self.subs.get(msg).remove(sub)

    def update(self):
        for msg in self.msg:
            for sub in self.subs.get(msg, []):
                sub.update(msg)
        self.msg = []

class Publisher:
    def __init__(self, provider):
        self.prov = provider

    def publish(self, msg):
        self.prov.put_msg(msg)


class Subscriber:
    def __init__(self, name, provider):
        self.name = name
        self.provider = provider

    def update(self, msg):
         print(self.name,'got',msg)

    def subscribe(self, msg):
        self.provider.subscribe(msg, self)

    def unsubscribe(self, msg):
        self.provider.unsubscribe(msg, self)


if __name__ == "__main__":
    msg_center = Provider()

    cctv = Publisher(msg_center)
    
    aa = Subscriber('aa', msg_center)
    bb = Subscriber('bb', msg_center)
    cc = Subscriber('cc', msg_center)

    aa.subscribe('joke')
    aa.subscribe('story')
    bb.subscribe('joke')
    cc.subscribe('story')

    cctv.publish('joke')
    cctv.publish('story')

    msg_center.update()

