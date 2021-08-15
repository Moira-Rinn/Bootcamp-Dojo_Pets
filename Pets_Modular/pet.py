from owner import Ninja, sacha


class Pet(Ninja):
    def __init__(self, owner, name, kind, tricks, energy):
        self.owner = owner
        self.name = name
        self.kind = kind
        self.tricks = tricks
        # self.health = health
        self.energy = energy

    def sleep(self):
        if self.is_dog:
            return f'*{self.name} makes bed and lays down*'
        # elif self == Cat:
        #     return f'*{self.name} needs on lap, lays down, purrrs*'

    def eat(self):
        if self.is_dog:
            return f'*{self.name} sniffs food and looks at {self.owner.first_name}*, *{self.name} reluctantly begins to eat*'
        # elif self == Cat:
        #     return f'*{self.name} sniffs food and looks at {self.owner.first_name}*, *{self.name} reluctantly begins to eat*'

    def play(self):
        if self.is_dog:
            return f'*{self.name} wants to play*'
        # elif self == Cat:
        #     return f'*{self.name} bats at string, looks at {sacha.first_name} with disdain*'

    def noise(self):
        if self.is_dog:
            return f'*{self.name} wimpers and barks*'


class Dog(Pet):
    def __init__(self, name, kind, tricks, is_dog=True):
        super().__init__(name, kind, tricks, )
        self.is_dog = is_dog


# class Cat(Pet):
#     def __init__(self, name, kind, tricks, health, energy, is_cat=True):
#         super().__init__(name, kind, tricks, energy)
#         self.is_cat = is_cat


sophie = Dog(sacha, 'Sophie', 'chihuahua', 'sit')


print(sacha.walk(sophie))
# print(sacha.feed(sophie))
# print(sacha.bathe(sophie))
# print(sophie.sleep())
