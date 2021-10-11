def f(a):
    b = a[0].copy()
    for i in range(1, len(a)):
        b = set(b).intersection(a[i])
    return list(b)


print(f([[1, 1, 1, 2, 2, 2, 3, 4, 5], [1, 2, 3, 5, 6, 7], [1, 2, 5], [1, 2, 3, 5]]))
