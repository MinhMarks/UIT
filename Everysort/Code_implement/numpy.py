import numpy as np

n = int(input())
arr = []
for i in range(n):
    num = float(input())
    arr.append(num)
arr = np.array(arr)
sorted_arr = np.sort(arr)
print(sorted_arr)