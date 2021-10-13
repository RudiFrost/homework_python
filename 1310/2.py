class Matrix:
    def __init__(self, matr):
        self.matr = matr
        min = len(matr[0])
        t = True
        for i in range(len(matr)):
            if len(matr[i]) != min:
                t = False
        if not t:
            print("._.")

    def transpone(self):
        newmatr = []
        i = 0
        for i in range(len(self.matr[i])):
            b = []
            for j in range(len(self.matr)):
                b.append(self.matr[j][i])
            newmatr.append(b)
        return newmatr


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
try:
    print(matrix.transpone())
except:
    print("А нормальную матрицу не пробовал задавать?")
