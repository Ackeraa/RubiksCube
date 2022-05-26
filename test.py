a = [1, 2, 3]
b = ["a", "b"]
for i in zip(a, b):
    print(i)
a = [(i, j) for i in range(2) for j in range(4)]
print(a)
