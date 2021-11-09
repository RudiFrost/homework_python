import string
import random

name = "Баобаб"
text = "    "
n = int(input())
for i in range(1, 1001):
    text += (random.choice(string.ascii_letters))
print(("{0:^" + "%s" % n + "s}").format(name))
a = 0
for i in range(1, 1001):
    if i % n == 0:
        print(text[a:i])
        a = i
