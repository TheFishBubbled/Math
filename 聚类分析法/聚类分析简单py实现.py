import numpy as np

# 以下为简单的欧氏距离的计算，可以通过修改向量的元素来获得n维向量之间的距离
point1 = np.array((1, 2, 3))
point2 = np.array((1, 1, 1))
dist1 = np.linalg.norm(point1 - point2)
print(dist1)

# np.linalg.norm()是NumPy中的一个函数，它用于计算向量或矩阵的范数（norm）。
# 它可以计算向量的L1范数、L2范数和无穷范数，也可以计算矩阵的Frobenius范数。
# np.linalg.norm(x, ord=None, axis=None, keepdims=False)
# 以下为常用方式：
# 计算向量的L2范数（欧几里得距离）：
dist2 = np.linalg.norm(point1)
print(dist2)
# 计算矩阵的Frobenius范数：
B= np.random.rand(3, 4)
dist3= np.linalg.norm(B)
print(dist3)
# 计算矩阵的列范数（列向量的L2范数）：
dist4= np.linalg.norm(  B, ord=2, axis=0)
print(dist4)
# 计算矩阵的行范数（行向量的L2范数）：
dist5= np.linalg.norm(B, ord=2, axis=1)
print(dist5)
# 计算向量的L1范数：
dist6= np.linalg.norm(point1, ord=1)
print(dist6)
# 计算向量的无穷范数：
dist7= np.linalg.norm(point1, ord=np.inf)
print(dist7)


# 以下的更为实用：
import numpy as np
from scipy.spatial.distance import pdist, squareform

A = np.random.rand(3, 4)  # 生成一个随机的n行m列矩阵

# 使用pdist函数计算每一对列向量之间的距离
distances = pdist(A.T)

# 将距离向量转换成距离矩阵
distance_matrix = squareform(distances)
print(distance_matrix)
