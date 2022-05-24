import numpy as np

a = np.ndarray((3, 3, 3), dtype=int)

for x in range(3):
    for y in range(3):
        for z in range(3):
            a[x, y, z] = y * 3 + z

a[0, :, :] = np.rot90(a[0, :, :], k=-1)
print(a[0, :, :])
