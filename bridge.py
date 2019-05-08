"""
桥接模式：
客户端提供一个中间人，去减少接口变化的影响
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