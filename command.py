"""
命令模式：
封装所有需要执行一个动作或者触发一个事件的信息(一个请求可以对应不同响应)

例子：
Django HttpRequest (without `execute` method):
 https://docs.djangoproject.com/en/2.1/ref/request-response/#httprequest-objects
"""

import os


class MovefileCommand:
    def __init__(self, src, des):
        self.src = src
        self.des = des

    def excute(self):
        self.rename(self.src, self.des)

    def rename(self, src, des):
        print('rename {} to {}'.format(src, des))
    
    def undo(self):
        self.rename(self.des, self.src)


if __name__ == "__main__":
    c = MovefileCommand('aa.txt', 'bb.txt')
    c.excute()
    c.undo()
