# Calculate the average (mean) of 2 NumPy arrays

import numpy as np


arr1 = np.array([1, 2, 3, 4])

arr2 = np.array([5, 6, 7, 8])

# 👇️ [ 6  8 10 12]
print(arr1 + arr2)

arr3 = (arr1 + arr2) / 2

# 👇️ [3. 4. 5. 6.]
print(arr3)