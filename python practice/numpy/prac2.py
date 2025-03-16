import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])

# Access first row
print(arr[0])

# Access specific element
print(arr[1, 2])  # Output: 60

# Slice: First 2 elements of first row
print(arr[0, :2])
