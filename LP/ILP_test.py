#此处时是对整数规划问题的一个实验，探索求解器是否能够求解整数规划（应该可以？）
import pulp
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
from pulp import LpSolverDefault

MyProbLP = pulp.LpProblem("LPProbDemo1", sense=pulp.LpMaximize)  # 求最大值
#本例子一共两个变量x1-x2
x1 = pulp.LpVariable('x1', lowBound=0 , cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0 ,cat='Integer')
#添加目标函数使用 "问题名 += 目标函数式" 格式。
MyProbLP +=  3*x1+2*x2
#添加约束条件使用
MyProbLP += ( 2*x1 + 3*x2  <= 14)  # 不等式约束
MyProbLP += ( 2*x1 + x2  <= 9)  # 不等式约束

#输出最简化
#LpSolverDefault.msg = 0
MyProbLP.solve()

for v in MyProbLP.variables():
 print(v.name, "=", v.varValue)  # 输出每个变量的最优值

print("Max z = ", pulp.value(MyProbLP.objective))  #输出最优解的目标函数值
#测试通过奥
