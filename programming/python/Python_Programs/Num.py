import numpy as np
a = np.array([2,3,4])
print(a.shape)
print(np.random.randint(100, size=(3,3)),)
for i in range(len(a)):
    print(a[i], end="")