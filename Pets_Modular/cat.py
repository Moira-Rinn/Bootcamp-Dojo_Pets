from pet import Pet


class Cat(Pet):
    def __init__(self, owner, name, kind, tricks, health, energy, ):
        super().__init__(owner, name, kind, tricks, health, energy)
