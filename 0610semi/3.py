import string


def f(a):
    b = {}
    for i in string.ascii_letters:
        b[i] = 0
    for i in a:
        if i in string.ascii_letters:
            b[i] = b[i] + 1
    return b


print(f(string.ascii_lowercase))
