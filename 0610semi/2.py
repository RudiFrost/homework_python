def create_region(name, city):
    a = {}
    for name, city in zip(name, city):
        a[name] = city
    return a


print(create_region(("sochi", "moscow"), {123: 321, 456: 654}))
