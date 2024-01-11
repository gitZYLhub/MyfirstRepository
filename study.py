import numpy as np

x = np.array([1, 2, 3, 4])
print(x.shape)
print(x)

x_add = x[:, np.newaxis]
print(x_add.shape)
print(x_add)

x_add_add = x_add.repeat(10, axis=0)

x_T = x_add.T
