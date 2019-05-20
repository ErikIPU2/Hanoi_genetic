from Hanoi import Hanoi
from random import randint

a = Hanoi(3)

movs = []

for i in range(1000):
    selN = randint(0, 2)
    toN = randint(0, 2)
    while selN == toN:
        toN = randint(0, 2)
    movs.append({"sel": selN, "to": toN})

print(movs)

a.set_movements(movs)

print(a.get_graphic(0))
print(a.get_graphic(1))
print(a.get_graphic(2))
