import string


def f(a):
    for i in string.punctuation:
        if i in a:
            a = a.replace(i, '')
    a = a.lower()
    b = set(a.split(" "))
    a = a.split(" ")
    print(a)
    k = {}
    for i in b:
        k[i] = 0
        for j in range(len(a)):
            if i == a[j]:
                k[i] = k[i] + 1
    k = sorted(k.items(), key=lambda x: x[1], reverse=True)
    try:
        for i in range(10):
            print(k[i][0], "повторяется", k[i][1], "раз")
    except:
        True


f("Для удаления пунктуации из строки Python воспользуемся методом строки str.replace(). А именно, в цикле пройдемся по всем символам пунктуации, и если они есть, то просто заменим его на пустую строку.")
