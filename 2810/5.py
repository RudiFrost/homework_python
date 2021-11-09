import matplotlib.pyplot as plt


def bar1():
    a = ""
    while a != "exit":
        xs = input("x: ")
        ys = input("y: ")
        color = input("Color(r, g, b): ")
        try:
            x = []
            y = []
            for i in xs.split():
                x.append(i)
            for i in ys.split():
                y.append(i)
            if color:
                plt.plot(x, y, color)
            else:
                plt.plot(x, y)
        except:
            print("._.")
        a = input("Введите exit, если хотите вывести график ")
    plt.show()


def bar2(*args, **kwargs):
    i = 1
    for list_1 in args:
        x, y = list_1[0], list_1[1]
        try:
            color = "color" + str(i)
            if color in kwargs.keys():
                plt.plot(x, y, color=kwargs[color])
            else:
                plt.plot(x, y)
        except:
            print("цвета: red, green, blue")
        i += 1
    plt.show()


def bar3(*args, **kwargs):
    try:
        x = args[0]
        y = args[1]
        barlist = plt.bar(x, y)
        for i in range(len(x)):
            color = "color" + str(i)
            if color in kwargs:
                barlist[i].set_color(kwargs[color])
    except:
        print("цвета: red, green, blue")
    plt.show()

def bar4(*args):
    sizes = []
    labels = []
    colors = []
    for size, label, color in args:
        sizes.append(size)
        labels.append(label)
        colors.append(color)
    plt.pie(sizes, colors=colors, startangle=180, autopct="%1.1f%%")
    plt.legend(labels, loc="best")
    man = plt.get_current_fig_manager()
    man.set_window_title("Diagnosis")
    plt.show()


def bar5(*args, **kwargs):
    try:
        x = args[0]
        y = args[1]
        barlist = plt.bar(x, y)
        for i in range(len(x)):
            color = "color" + str(i)
            if color in kwargs:
                barlist[i].set_color(kwargs[color])
    except Exception as e:
        print(e)
    plt.show()
