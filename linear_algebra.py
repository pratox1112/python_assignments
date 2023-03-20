import numpy as np
n=int(input())
a=np.array([input().split() for _ in range(n)],float)
np.set_printoptions(legacy='1.13')
print(np.linalg.det(a))
