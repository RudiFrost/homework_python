import random


class Parent:
    def __init__(self, name, eye, hair):
        self.name = name
        self.eye = eye
        self.hair = hair


class Child:
    def __init__(self, name, par1, par2):
        self.name = name
        eyes = [par1.eye, par2.eye]
        hairs = [par1.hair, par2.hair]
        self.eye = random.choice(eyes)
        self.hair = random.choice(hairs)



p1 = Parent("Ggg", "green", "brown")
p2 = Parent("Kkk", "blue", "blonde")
c1 = Child("Lll", p1, p2)
print(c1.name)
print(c1.eye)
print(c1.hair)
