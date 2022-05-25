a =  {"y": 2, "z": 1, "x": 3}
for value in sorted(a.values(), key=lambda value:-value):
    print(value)
