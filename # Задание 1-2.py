# Задание 1
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.components = []
    def __str__(self):
        components = ", ".join(self.components) or "нет"
        return (
            f"Компьютер: CPU - {self.cpu}, RAM = {self.ram}, "
            f"Storage = {self.storage}, GPU - {self.gpu}, "
            f"комплектующие: {components}"
        )
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    def set_ram(self, ram):
        self.computer.ram = ram
        return self
    def set_storage(self, storage):
        self.computer.storage = storage
        return self
    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self
    def add_component(self, component):
        self.computer.components.append(component)
        return self
    def build(self):
        return self.computer

builder = ComputerBuilder()
computer = (builder.set_cpu("Intel Core i7-13700K")
    .set_ram("32 ГБ DDR5")
    .set_storage("1 ТБ NVMe SSD")
    .set_gpu("NVIDIA RTX 4070")
    .add_component("Блок питания 750 Вт")
    .add_component("Корпус ATX")
    .add_component("Кулер для процессора")
    .build()
)
print(computer)

# Задание 2
from abc import ABC, abstractmethod
class Action(ABC):
    @abstractmethod
    def perform(self, name):
        pass
class Meow(Action):
    def perform(self, name):
        print(f"{name} мяукает: Мяу!")
class Fly(Action):
    def perform(self, name):
        print(f"{name} летает: Вжух!")
class Animal:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
    def do_action(self):
        self.strategy.perform(self.name)
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, Meow())
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, Fly())

cat = Cat("Барсик")
bird = Bird("Кеша")

cat.do_action()
bird.do_action()