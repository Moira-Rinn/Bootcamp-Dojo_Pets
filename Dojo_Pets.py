class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self, pet):
        return (
            f"{self.pet}! Let's go for a walk.",
            pet.play()
        )

    def feed(self, pet):
        return (
            f"{self.pet}! get your nummies!",
            pet.eat()
        )

    def bathe(self, pet):
        return (
            f"*{self.first_name}*fills tub with water* {self.pet} wanna take a bath?",
            pet.noise()
        )


class Pet(Ninja):
    def __init__(self, name, kind, tricks, health, energy):
        # super().__init__(first_name, last_name, pet, treats, pet_food)
        self.name = name
        self.kind = kind
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        return f'*{self.name} makes bed and lays down*'

    def eat(self):
        return f'*{self.name} sniffs food and looks at {sacha.first_name}*, *{self.name} reluctantly begins to eat*'

    def play(self):
        return f'*{self.name} wants to play*'

    def noise(self):
        return f'*{self.name} wimpers and barks*'


sophie = Pet('Sophie', 'chihuahua', 'sit', health=100, energy=100)
sacha = Ninja('Sacha', 'Rinn', sophie.name, 'chicken', 'kibble')


print(sacha.walk(sophie))
print(sacha.feed(sophie))
print(sacha.bathe(sophie))
