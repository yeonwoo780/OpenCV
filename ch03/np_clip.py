import numpy as np

arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
## 3333~777

arr2 = np.clip(arr1, 3, 7)

print(arr2)