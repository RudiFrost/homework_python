import matplotlib.pyplot as plt

def bar1():
    a = ""
    while a != 'exit':
        xs = input('x: ')
        ys = input('y: ')
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
            print('._.')
        a = input('Введите exit, если хотите вывести график ')
    plt.show()

bar1()