#Importando o Modulo
import random

print(random.randint(1, 100))
print(random.random())
print(random.uniform(10, 20))

itens = ["Python", "Java", "C++"]
print(random.choice(itens))

random.shuffle(itens)
print(itens)