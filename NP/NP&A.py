#此处代码在于求解非线性问题，另外的一个问题在于，我能不能在py中画出一个多元函数的图像？

#在使用 Python 求解非线性规划时要注意求解器的适用范围， 需要注意的是scipy函数除了线性的问题都可以求解（? 有点废话的意思）
#值得注意的是，scipy的minimize函数求解的是局部最优解，为了得到最佳解，最好进行随机循环

#以下介绍scipy.optimize.minimize 函数

#导入库，以下对参数进行解释

from scipy.optimize import minimize
import numpy as np
#res = scipy.optimize.minimize(fun, x0, args=(), method=None, jac=None,
# hess=None, hessp=None, bounds=None, constraints=(), tol=None, callback=None, options=None)
struct = np.dtype([
    ('X', np.float64, 3),
    ('f', np.float64),
])
#要注意，范围与数组范围一致！
StoryData = np.empty((100,), dtype=struct)
for i in range(0,100):

    # fun：优化问题的目标函数，它的输入是一个一维 NumPy 数组，输出是一个标量。
    # 以下是举例，fun的输入是一个数组
    # lambda函数是一种匿名函数，可以快速定义简单的函数。它通常用于需要定义一个简单函数来在另一个函数中使用，而不需要单独定义一个函数。
    # np.dot()向量点乘或矩阵乘法
    # 此处定义的结果是，obj返回x的平方+8
    obj = lambda x: x[0]**2 + x[1]**2 + x[2]**2 + 8

    # x0: 初值, 一维 NumPy 数组
    # 以下给出rand 函数几个示例：
    # np.random.rand(a, b)：随机生成一个a*b的函数
    # np.random.randint(a, b, size=(c, d))：随机生成一个范围为（c,d）的整数矩阵，矩阵大小为a,b
    # np.random.binomial(n,p,size=N)：

    x0 = 10*np.random.rand(1, 3)
    x0 = x0.ravel()
    # x0=np.array([0.0,1.0,0.0])
    # method: 求解器的类型，默认时自动选择合适的求解方式
    method = None
    # constraints: 求解器 SLSQP 的约束被定义为字典的列表，字典用到的字段主要有：
    # 'type': str: 约束类型：“eq” 表示等式，“ineq” 表示不等式 (SLSQP 的不等式约束是 f ( x ) ≥ 0 f(x)\geq 0f(x)≥0 的形式)
    # 'fun': 可调用的函数或匿名函数：定义约束的函数

    # cons=[{'type':'ineq','fun':lambda x: G(x)},{'type':'eq','fun':lambda x: H(x)}]
    # 要注意的是，不等式约束是一个>=0的条件

    cons = [{'type': 'ineq', 'fun': lambda x: x[0]**2 - x[1] +x[2]**2},
            {'type': 'ineq', 'fun': lambda x: 20- x[0] - x[1]**2 - x[2]**2},
            {'type': 'eq', 'fun': lambda x: x[0] + x[1]**2 -2 },
            {'type': 'eq', 'fun': lambda x: x[1] + 2* x[2]**2 - 3}]

    # 定义变量界
    bd = [(0, None), (0, None), (0, None)]

    #
    res = minimize(obj, x0, constraints=cons, bounds=bd)

    print(res.fun)  # 最优值
    print(res.success)  # 求解状态
    print(res.x)  # 最优解
    StoryData[i]['X']=res.x
    StoryData[i]['f']=res.fun

print("  ")
min_index = np.argmin(StoryData['f'])
print("最小的情况为：",StoryData[min_index])

#√
#所有的非线性问题都可以进入此类