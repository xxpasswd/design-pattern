"""
建造者模式：
将一个复杂对象的构建过程和表示分离开来

优点：
1. 客户端不必知道对象的内部细节，将对象本身和创建过程解耦
2. 精确的控制复杂对象的创建过程

适用场景：
1. 需要生成的对象有复杂的内部结构
2. 生产的对象的属性相互依赖，需要指定其生产顺序
3. 将对象的构建过程和表示分离开来
"""

class Building:
    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError


class House(Building):
    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big'

    def __str__(self):
        return 'floor is {}, size is {}'.format(self.floor, self.size)


# 上面是将构造过程放到了类的__init__方法里面了，在一些复杂的对象里面，我们需要将构
# 过程和类分离开来

class ComplexBuilding:
    def build_floor(self):
        self.floor = 'Two'

    def build_size(self):
        self.size = 'small'

    def __str__(self):
        return f'floor is {self.floor}, size is {self.size}'


def constructs_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building


if __name__ == "__main__":
    house = House()
    print(house)
    complex_building = constructs_building(ComplexBuilding)
    print(complex_building)
