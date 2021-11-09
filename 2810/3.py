import matplotlib.pyplot as plt


def draw_pie(*args):
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


draw_pie((119, "blood", "red"), (20, "sea", "b"), (40, "greenpeace", "green"), (20, "malovar", "yellow"))
