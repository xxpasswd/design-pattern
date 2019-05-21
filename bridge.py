"""
桥接模式：
客户端提供一个中间人，去减少接口变化的影响（将抽象部分和与其实现部分分离，使他们都可以独立的
变化）

优点：
1. 分离了抽象和实现部分，使抽象和实现部分能够各自变化
2. 在很多情况下，桥接模式能够取代多层继承方案
3. 桥接模式提高了系统的可扩展性，在抽像和实现部分任意扩展，都不影响原系统

应用场景：
系统有多个维度的变化因素，可以将每个维度分离开来，使用桥接模式
"""
class DrawingApi1:
    def draw_circle(self, x, y, radius):
        print('DrawApi1 draw', x, y, radius, 'circle')


class DrawingApi2:
    def draw_circle(self, x, y, radius):
        print('DrawApi2 draw', x, y, radius, 'circle')


class CircleShape:
    def __init__(self, x, y, radius, drawing_api):
        self.drawing_api = drawing_api
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)


if __name__ == "__main__":
    drawing_api1 = DrawingApi1()
    drawing_api2 = DrawingApi2()
    
    shapes = [CircleShape(1,2,3, drawing_api1), CircleShape(1,2,3, drawing_api2)]

    for shape in shapes:
        shape.draw()