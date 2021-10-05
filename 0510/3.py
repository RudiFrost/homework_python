def f(a):
    if a[0].isupper() and a[1:].islower():
        return True
    return False


print(f("Rudolf"))
