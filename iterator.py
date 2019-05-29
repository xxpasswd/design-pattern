"""
迭代器模式：
提供一种方法访问聚合对象，而不用暴露聚合对象的内部表示。就是给聚合对象提供一个迭代器，让访问通过迭代器进行。

优点：
1. 一个聚合对象就可以通过多种不同的迭代器来访问
2. 将聚合对象和迭代器的职责分离了开来，设计更加灵活

应用场景：
1. 访问一个聚合对象，无需暴漏它的内部表示
2. 给一个聚合对象，提供多种不同的迭代方式

实例：
django的分页对象Paginator
"""


def count_to(alist, count):
    for i in alist[:count]:
        yield i


if __name__ == "__main__":
    alist = ['one', 'two', 'three', 'four', 'five']

    for i in count_to(alist, 2):
        print(i)

    for i in count_to(alist, 5):
        print(i)