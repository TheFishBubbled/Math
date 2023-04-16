#Homework_1
#第一种情况，给定一个风险度，在风险度内输出
import pulp
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
from pulp import LpSolverDefault

MyProbLP = pulp.LpProblem("LPProbDemo1", sense=pulp.LpMaximize)  # 求最大值
#本例子一共九个变量x1-x9
x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0 ,cat='Integer')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Integer')
x4 = pulp.LpVariable('x4', lowBound=0, cat='Integer')
x5 = pulp.LpVariable('x5', lowBound=0, cat='Integer')
x6 = pulp.LpVariable('x6', lowBound=0, cat='Integer')
x7 = pulp.LpVariable('x7', lowBound=0 ,cat='Integer')
x8 = pulp.LpVariable('x8', lowBound=0, cat='Integer')
x9 = pulp.LpVariable('x9', lowBound=0, cat='Integer')
#添加目标函数使用 "问题名 += 目标函数式" 格式。
MyProbLP +=((x4-x7)+(x3-x6)+x5)+1.65*x6+2.3*x7-((5*x7+10*(x1-x7))*(300.0/6000.0)+(7*x9+9*(x2-x9-x7)+12*x7)*(321.0/10000.0)+(6*(x3-x6)+8*x6)*(250.0/4000.0)+(4*(x4-x7)+11*x7)*(783.0/7000.0)+(7*x5)*(200.0/4000.0))# 设置目标函数
#添加约束条件使用
MyProbLP += (5*x7+10*(x1-x7)<=6000)  # 不等式约束
MyProbLP += (7*x9+9*(x2-x9-x7)+12*x7 <=10000)  # 不等式约束
MyProbLP += (6*(x3-x6)+8*x6<= 4000)  # 不等式约束
MyProbLP += (4*(x4-x7)+11*x7 <= 7000)  # 不等式约束
MyProbLP += (7*x5<= 4000)  # 不等式约束
MyProbLP += (x1+x2-x3-x4-x5==0)  # 等式约束
MyProbLP += ((x1-x8)+(x2-x7-x9)-x6==0)  # 等式约束
#输出最简化
#LpSolverDefault.msg = 0
MyProbLP.solve()
arr=np.empty(9)
i=0
for v in MyProbLP.variables():
 print(v.name, "=", v.varValue)  # 输出每个变量的最优值
 arr[i]=v.value()
 i=i+1
print("Max F(x) = ", pulp.value(MyProbLP.objective))  #输出最优解的目标函数值
print("Ⅰ应该生产：",arr[3]+arr[4]+arr[2]-arr[6]-arr[5])
print("Ⅱ应该生产：",arr[5])
print("Ⅲ应该生产：",arr[6])
print(" ")
print("答案有待考证")

