def valid(a):
    return a[0].isupper() and a[1:].islower()


def f():
    b = []
    c = ""
    while c != "q":
        c = input()
        if c != "q":
            if valid(c):
                b.append(c)
    return b


print(f())
