import numpy as np
n, m = list(map(int, input() .split()))
arr =np.array([input().split() for i in range(n)], dtype=int)
minofaxis=np.min(arr ,axis=1)
print(max(minofaxis))
