class Game:
    def __init__(self, length):
        self.length = length

    def play(self, n, car):
        self.car = car
        b = []
        a = []
        for c in self.car:
            b.append(c.speed)
        for j in range(len(self.car)):
            max = 0

            for i in range(len(self.car)):
                if b[i] > b[max]:
                    max = i
            for i in range(len(self.car)):
                if b[i] == b[max]:
                    b[i] = 0
            a.append(self.car[max].name)
        return a


class Car:
    def __init__(self, speed, name):
        self.speed = speed
        self.name = name


c1 = Car(12, "qwe")
c2 = Car(15, "asd")
c3 = Car(10, "zxc")
c4 = Car(11, "rty")
c5 = Car(20, "fgh")
g = Game(100)
print(g.play(5, [c1, c2, c3, c4, c5]))
