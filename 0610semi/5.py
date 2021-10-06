def f():
    c = {}
    a = 0
    while a != "q":
        a = input()
        if a == "q":
            break
        b = input()
        if len(b) == 16:
            if b[0] == "+" and b[1].isdigit() and b[2] == "-" and b[6] == "-" and b[10] == "-" and b[
                13] == "-" and b[3:6].isdigit() and b[7:10].isdigit() and b[11:13].isdigit() and b[14:17]:
                c[a] = b
            else:
                print("Давай все по новой")
        else:
            print("Давай все по новой")
    print(c)

f()
