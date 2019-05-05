"""
分离数据显示，应用逻辑和数据管理
"""
class Data:
    """
    数据层
    """
    pets = {
        'dog': {'age': 4, 'color': 'white'},
        'cat': {'age': 3, 'color': 'yellow'}
    }

    def __get__(self, instance, owner):
        print('get pets data from Data')
        return {'pets': self.pets}


class BussinessLogic:
    """
    业务逻辑层
    """
    data = Data()

    def get_pet_list(self):
        return self.data['pets'].keys()

    def pet_info(self, pet):
        return self.data['pets'].get(pet, None)


class Ui:
    """
    数据展示层
    """
    def __init__(self):
        self.b = BussinessLogic()

    def get_pet_list(self):
        print('pets list are:')
        for pet in self.b.get_pet_list():
            print(pet)

    def get_pet_info(self, pet):
        pet_info = self.b.pet_info(pet)
        if pet_info:
            print(pet_info)
        else:
            print('not such pet')


if __name__ == "__main__":
    u = Ui()
    u.get_pet_list()
    u.get_pet_info('dog')
    u.get_pet_info('pig')
