"""
抽象工厂模式：
提供一个创建一系列相关对象或依赖对象的接口

优点：
1. 隔离了对象的创建和使用过程
2. 当多个对象一起使用时，保证每次创建的多个对象是相关的

应用场景：
需要创建一组相关的对象，而不用关心它们的创建细节
"""
class WindowsOperationController:
    """游戏操作控制类"""
    def move(self):
        print('move action depends on windows')


class WindowsInterfaceController:
    """游戏界面控制类"""
    def dispaly(self):
        print('dispaly depends on windows')


class MacOperationController:
    def move(self):
        print('move action depends on mac')


class MacInterfaceController:
    def dispaly(self):
        print('dispaly depends on mac')


class WindowsControllerFactory:
    def get_operation_controller(self):
        return WindowsOperationController()

    def get_interface_controller(self):
        return WindowsInterfaceController()


class MacControllerFactory:
    def get_operation_controller(self):
        return MacOperationController()

    def get_interface_controller(self):
        return MacInterfaceController()


def get_factory(system):
    factory = {
        "windows": WindowsControllerFactory(),
        "mac": MacControllerFactory()
    }
    return factory[system]


if __name__ == "__main__":
    windows = get_factory('windows')
    windows.get_operation_controller().move()
    windows.get_interface_controller().dispaly()

    mac = get_factory('mac')
    mac.get_operation_controller().move()
    mac.get_interface_controller().dispaly()
