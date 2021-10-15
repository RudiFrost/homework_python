def f(list, alligment, count, filler):
    if alligment == "center":
        alligment = "^"
    elif alligment == "left":
        alligment = "<"
    elif alligment == "right":
        alligment = ">"
    try:
        for i in list:
            print(("{0:" + filler + alligment + "%s" % count + "s}").format(i))
    except:
        print("._.")


f(["a", "b", "c"], "right", 30, "-")
