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
            f"*{self.first_name} fills tub with water* {pet.name} wanna take a bath?",
            pet.noise()
        )


sacha = Ninja('Sacha', 'Rinn', "Sophie", 'chicken', 'kibble')
