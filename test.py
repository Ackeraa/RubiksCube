import numpy as np

class A:
    def __init__(self):
        self._items = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)]

    def __getitem__(self, x, y):
        print(x, y)


a = A()
a[0][1]
