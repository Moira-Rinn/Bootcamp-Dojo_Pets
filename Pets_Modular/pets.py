from owner import sacha
from dog import Dog
from cat import Cat

sophie = Dog(sacha, 'Sophie', 'dog', 'sit', health=100, energy=100)
debbie = Cat(sacha, 'Debbie', 'cat', 'annoyed stare', health=100, energy=100)


print(sacha.walk(sophie))
print(sacha.walk(debbie))
print(sacha.feed(sophie))
print(sacha.feed(debbie))
print(sacha.bathe(sophie))
print(sacha.bathe(debbie))
print(sophie.sleep())
print(debbie.sleep())
