from owner import Ninja, sacha


class Pet(Ninja):
    def __init__(self, owner, name, kind, tricks, health, energy):
        self.owner = owner
        self.name = name
        self.kind = kind
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        if self.kind == 'dog':
            return f'*{self.name} makes bed and lays down*'
        elif self.kind == 'cat':
            return f'*{self.name} needs on lap, lays down, purrrs*'

    def eat(self):
        if self.kind == 'dog':
            return f'*{self.name} sniffs food, wags tail, and looks at {self.owner.first_name}*, *{self.name} Begins to inhale food*'
        elif self.kind == 'cat':
            return f'*{self.name} sniffs food and looks at {self.owner.first_name} with mild disappointment*, *{self.name} reluctantly begins to eat*'

    def play(self):
        if self.kind == 'dog':
            return f'*{self.name} wants to play*'
        elif self.kind == 'cat':
            return f'*{self.name} bats at string, looks at {sacha.first_name} with disdain*'

    def noise(self):
        if self.kind == 'dog':
            return f'*{self.name} wimpers and barks*'
        elif self.kind == 'cat':
            return f'*{self.name} hisses and growls*'
