def f(a):
    q = []
    for i in range(len(a)):
        b = a[i].split(" ")
        c = b[0] + " " + b[1][0] + "." + b[2][0] + "."
        q.append(c)
    return q


print(f(["Kebu Rudolf Eduardovich", "Ku Rudolf Eduardovich", "Ku Oudolf Eduardovich"]))
