def f(a):
    b = a[0].isupper()
    for i in range(1, len(a)):
        c = a[i].islower()
        if c:
            continue
        else:
            return False
            break
    if b and c:
        return True
    return False


print(f("Rudolf"))
