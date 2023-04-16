# Homework_1
# 第一种情况，给定一个风险度，在风险度内输出
import pulp
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
from pulp import LpSolverDefault

MyProbLP = pulp.LpProblem("LPProbDemo1", sense=pulp.LpMaximize)  # 求最大值
# 本例子一共20个变量x11-x45
x11 = pulp.LpVariable('x11', lowBound=0, cat='Integer')
x12 = pulp.LpVariable('x12', lowBound=0, cat='Integer')
x13 = pulp.LpVariable('x13', lowBound=0, cat='Integer')
x14 = pulp.LpVariable('x14', lowBound=0, cat='Integer')
x15 = pulp.LpVariable('x15', lowBound=0, cat='Integer')

x21 = pulp.LpVariable('x21', lowBound=0, cat='Integer')
x22 = pulp.LpVariable('x22', lowBound=0, cat='Integer')
x23 = pulp.LpVariable('x23', lowBound=0, cat='Integer')
x24 = pulp.LpVariable('x24', lowBound=0, cat='Integer')
x25 = pulp.LpVariable('x25', lowBound=0, cat='Integer')

x31 = pulp.LpVariable('x31', lowBound=0, cat='Integer')
x32 = pulp.LpVariable('x32', lowBound=0, cat='Integer')
x33 = pulp.LpVariable('x33', lowBound=0, cat='Integer')
x34 = pulp.LpVariable('x34', lowBound=0, cat='Integer')
x35 = pulp.LpVariable('x35', lowBound=0, cat='Integer')

x41 = pulp.LpVariable('x41', lowBound=0, cat='Integer')
x42 = pulp.LpVariable('x42', lowBound=0, cat='Integer')
x43 = pulp.LpVariable('x43', lowBound=0, cat='Integer')
x44 = pulp.LpVariable('x44', lowBound=0, cat='Integer')
x45 = pulp.LpVariable('x45', lowBound=0, cat='Integer')

# 添加目标函数使用 "问题名 += 目标函数式" 格式。
MyProbLP += 7 * (x11 + x12 + x13 + x14 + x15) + 8 * (x21 + x22 + x23 + x24 + x25) + 9 * (
            x31 + x32 + x33 + x34 + x35) + 7 * (x41 + x42 + x43 + x44 + x45)
# 添加约束条件使用
MyProbLP += (1.3 * x11 + 1.8 * x21 + 1.3 * x31 + 0.9 * x41 <= 4500)  # 不等式约束
MyProbLP += (0.9 * x12 + 1.7 * x22 + 1.2 * x32 + 1.1 * x42 <= 5000)  # 不等式约束
MyProbLP += (2 * x13 + 1.4 * x23 + 1.3 * x33 + 1 * x43 <= 4500)  # 不等式约束
MyProbLP += (0.3 * x14 + 0.6 * x24 + 1.0 * x34 + 0.9 * x44 <= 1500)  # 不等式约束
MyProbLP += (0.9 * x15 + 1.1 * x25 + 1.4 * x35 + 1 * x45 <= 2500)  # 不等式约束

# 输出最简化
# LpSolverDefault.msg = 0
MyProbLP.solve()
arr = np.empty(20)
i = 0
for v in MyProbLP.variables():
    print(v.name, "=", v.varValue)  # 输出每个变量的最优值
    arr[i] = v.value()
    i = i + 1
print("Max F(x) = ", pulp.value(MyProbLP.objective))  # 输出最优解的目标函数值
print("P1应该生产：", arr[0] + arr[1] + arr[2] + arr[3]+arr[4] )
print("P2应该生产：", arr[5] + arr[6] + arr[7] + arr[8]+arr[9]  )
print("P3应该生产：",arr[10] + arr[11] + arr[12] + arr[13]+arr[14] )
print("P4应该生产：",arr[15] + arr[16] + arr[17] + arr[18]+arr[19]  )


print("L1的剩余时间为：",4500-(1.3 * arr[0] + 1.8 * arr[5] + 1.3 * arr[10] + 0.9 * arr[15]))
print("L2的剩余时间为：",5000-(0.9 * arr[1] + 1.7 * arr[6] + 1.2 * arr[11] + 1.1 * arr[16]))
print("L3的剩余时间为：",4500-(2.0 * arr[2] + 1.4 * arr[7] + 1.3 * arr[12] + 1.0 * arr[17]))
print("L4的剩余时间为：",1500-(0.3 * arr[3] + 0.6 * arr[8] + 1.0 * arr[13] + 0.9 * arr[18]))
print("L5的剩余时间为：",2500-(0.9 * arr[4] + 1.1 * arr[9] + 1.4 * arr[14] + 1.0 * arr[19]))