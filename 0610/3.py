def f(a):
    for i in set(a):
        k = 0
        for j in a:
            if i == j:
                k += 1
        if k > 1:
            o = str(i) + " Повторяется " + str(k) + " раз"
            yield o


for i in f([1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 6]):
    print(i)
