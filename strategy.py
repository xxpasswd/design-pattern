"""
策略模式：
定义一系列算法，将这些算法封装起来，并让他们可以互相替换

应用场景：
1. 一个系统需要动态的从算法中选择一种算法
2. 一个对象有很多行为，可以使用策略模式，避免使用多重选择语句
"""

class Order:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy


    def price_after_discount(self):
        if self.discount_strategy:
            return self.discount_strategy().calculate(self.price)
        else:
            return 0

    def __str__(self):
        return 'price {}, after discount {}'.format(self.price, self.price_after_discount())


class TenPercentStrategy:
    def calculate(self, price):
        return price * 0.1


class SaleStrategy:
    def calculate(self, price):
        return price * 0.5


if __name__ == "__main__":
    o1 = Order(12, TenPercentStrategy)
    o2 = Order(12, SaleStrategy)

    print(o1)
    print(o2) 
