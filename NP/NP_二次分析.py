from scipy.optimize import minimize
import numpy as np

H = np.array([[4, -4], [-4, 8]])
f = np.array([[-6], [-3]])


def obj(x):
    return 0.5 * np.dot(x, np.dot(H, x)) + np.dot(f.ravel(), x)


method = 'SLSQP'

b = np.array([[3], [9]])
A = np.array([[1, 1], [4, 1]])


def cons(x):
    return b.ravel() - np.dot(A, x)


bd = [(0, None), (0, None)]

results = []

for i in range(100):
    x0 = 10 * np.random.rand(2)
    res = minimize(obj, x0, method=method, constraints={'type': 'ineq', 'fun': cons}, bounds=bd)
    results.append({'x': res.x, 'fun': res.fun})
    print(f"Iteration {i + 1}: {res.fun}")

    print(res.fun)  # 最优值
    print(res.success)  # 求解状态
    print(res.x)  # 最优解

print("  ")
min_index = np.argmin(results[i])
print("最小的情况为：",results[min_index])
