"""
中介者模式：
用一个中介对象来封装一系列对象的交互，从而使各个对象之间降低耦合度。

应用场景：
系统中有很多对象，需要多对多之间通信，通过中介者来协调
"""


class ChatRoom:
    def dispaly_message(self, user, msg):
        print('{} say {}'.format(user, msg))


class User:
    def __init__(self, name):
        self.name = name
        self.chatroom = ChatRoom()

    def say(self, msg):
        self.chatroom.dispaly_message(self, msg)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    linda = User('linda')
    Tom = User('Tom')
    Dowen = User('Dowen')

    linda.say('hello')
    Tom.say('welcome')
    Dowen.say('good')