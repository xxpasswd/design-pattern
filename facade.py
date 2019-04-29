"""
外观模式：
提供一个统一的接口给外界，封装接口内部的复杂变化
"""

class CPU:
    """
    simple cpu representation
    """
    def freeze(self):
        print('Freezing porccessor')

    def jump(self, position):
        print('Jump to:', position)

    def execute(self):
        print('Executing')


class Memory:
    """
    Simple memory representation.
    """
    def load(self, position, data):
        print("Loading from {0} data: '{1}'.".format(position, data))


class SolidStateDrive:
    """
    Simple solid state drive representation.
    """
    def read(self, lba, size):
        return "Some data from sector {0} with size {1}".format(lba, size)


class ComputerFacade:
    """
    Represents a facade for various computer parts.
    """
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start()
