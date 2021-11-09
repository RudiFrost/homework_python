import string
import random


def gen_string(n):
    length = ""
    for i in range(n):
        length += (random.choice(string.ascii_letters))
    return length


def counter(length):
    low = 0
    cap = 0
    for i in length:
        if i in string.ascii_lowercase:
            low += 1
        elif i in string.ascii_uppercase:
            cap += 1
    if cap > low:
        return 1
    elif cap < low:
        return -1
    return 0


def f(list_1):
    kol_1 = 0
    kol_0 = 0
    for i in list_1:
        c = counter(i)
        if c == 1:
            kol_1 += 1
        elif c == 0:
            kol_0 += 1
    print('Процент количества строк, в которых больше заглавных букв: ',
          round(kol_1 * 100 / len(list_1), 1), "%", sep="")
    print('Процент количества строк, в которых больше маленьких букв: ',
          round((len(list_1) - kol_1 - kol_0) * 100 / len(list_1), 1), "%", sep="")
    print('Процент количества строк, в которых одинаковое число заглавных и маленьких букв: ',
          round(kol_0 * 100 / len(list_1), 1), "%", sep="")


f([gen_string(45), gen_string(45), gen_string(45), gen_string(45), gen_string(4), gen_string(10), gen_string(3),
   gen_string(17), gen_string(105), gen_string(45), gen_string(5), gen_string(4)])
