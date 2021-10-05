def f():
    b = []
    c = ""
    while c != "q":
        c = input()
        if c != "q":
            b.append(c)
    return b


print(f())
