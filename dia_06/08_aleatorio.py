import random

x = ["Téo", "Maria", "Jose", "Ana", "Joao"]

valor_1 = random.choice(x)
x.remove(valor_1)
print("Removido:", valor_1)

valor_2 = random.choice(x)
x.remove(valor_2)
print("Removido:", valor_2)

print("Lista final:", x)
