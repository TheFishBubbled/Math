#第一种情况，给定一个风险度，在风险度内输出
import pulp
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
import matplotlib.pyplot as plt
#定义一个结构体和数组，有助于最后查看最大最小值
from pulp import LpSolverDefault
#定义结构体
struct = np.dtype([
    ('X', np.float64, 5),
    ('f', np.float64),
    ('a', np.float64)
])
arr = np.empty((1001,), dtype=struct)
#此处由于需要参变量改变值，故进行一个循环输出
for a in range(0, 1001):
 #第一个是arr的循环变量
 i=a
 #第二个是a从0到0.001
 a = a / 1000.0
 MyProbLP = pulp.LpProblem("LPProbDemo1", sense=pulp.LpMaximize)  # 求最大值
#本例子一共五个变量x0-x4
 x0 = pulp.LpVariable('x0', lowBound=0, cat='Continuous')
 x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
 x2 = pulp.LpVariable('x2', lowBound=0 ,cat='Continuous')
 x3 = pulp.LpVariable('x3', lowBound=0, cat='Continuous')
 x4 = pulp.LpVariable('x4', lowBound=0, cat='Continuous')
#添加目标函数使用 "问题名 += 目标函数式" 格式。
 MyProbLP += 0.05*x0+0.27*x1+0.19*x2+0.185*x3+0.185*x4	# 设置目标函数
#添加约束条件使用
 MyProbLP += (0.025*x1<= a)  # 不等式约束
 MyProbLP += (0.015*x2 <= a)  # 不等式约束
 MyProbLP += (0.055*x3<= a)  # 不等式约束
 MyProbLP += (0.026*x4 <= a)  # 不等式约束
 MyProbLP += (x0+1.01*x1+1.02*x2+1.045*x3+1.065*x4 == 1)  # 等式约束

#输出最简化
 LpSolverDefault.msg = 0
 MyProbLP.solve()
 print('a=',a)
 j=0
 for v in MyProbLP.variables():
    arr[i]['X'][j]=v.value()
    print(v.name, "=", v.varValue)  # 输出每个变量的最优值
    j=j+1
 print("Max F(x) = ", pulp.value(MyProbLP.objective))  #输出最优解的目标函数值
 print(" ")
 arr[i]['f']=pulp.value(MyProbLP.objective)
 arr[i]['a']=a


a_values = arr['a']
f_values = arr['f']

fig = go.Figure(data=go.Scatter(x=a_values, y=f_values, mode='markers'))
fig.update_layout(xaxis=dict(tickmode='linear', tick0=0, dtick=0.01),
                  yaxis=dict(range=[0, 0.3]),
                  xaxis_title='a',
                  yaxis_title='f')
pio.show(fig)

max_index = np.argmax(arr['f'])
print(arr[max_index])



#输出
with open('output.txt', 'w') as f:
    for item in arr:
        x_str = str(item[0]).ljust(20)
        f_str = str(item[1]).ljust(20)
        a_str = str(item[2]).ljust(20)
        f.write(f'{x_str}{f_str}{a_str}\n')