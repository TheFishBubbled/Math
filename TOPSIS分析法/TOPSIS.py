# 理想解法--评价指标一定不唯一
# 通过构建最优解和最劣解，计算每个方案到理想方案的相对贴进度，对方案进行排序，选出最优方案

# 方法原理：多属性决策方案集为D，衡量方案优劣的属性变量为x1，x2，每个方案n个属性构成的向量是n维空间的一个点
# 正理想解C是方案集D中并不存在的虚拟 最佳方案，每个值都是决策矩阵中属性最好的值
# 负理想解是虚拟的最差方案，每个属性都是最差值，根据比较距离，最靠近正最远离负为最佳方案
# 欧几里得空间距离（？）

# 重点在于虚构最佳的理想解，正理想是每个方案最佳的集合，负理想是每个方案最差
# 1.求出规范决策矩阵 2.构成加权规范矩阵 3.确定正理想解和负理想解（需要考虑是效益还是成本来取最大或者最小值）
# 4.计算欧氏距离 5.计算各个方案的排队指标值 6.由大到小排列指标值来选出方案优劣

# 在这里需要注意的是，我们需要对原始数据集中的指标属性同向化（均转变为最大值是最好的）
# 一般情况下有四类指标：极大型，极小型，中间型，区间型。一般我们将其都转换为最大型（正向）

import pandas as pd
import numpy as np


# 以下函数输入是一个数组，返回也是一个数组
# 正向化评价指标
def datadirection_1(datas, offset=0):  # 极小型 ->极大型
    def normalization(data):
        return 1 / (data + offset)

    return list(map(normalization, datas))


def datadirection_2(datas, x_min, x_max):  # 中间型->极大型
    def normalization(data):
        if data <= x_min or data >= x_max:
            return 0
        elif data > x_min and data < (x_min + x_max) / 2:
            return 2 * (data - x_min) / (x_max - x_min)
        elif data < x_max and data >= (x_min + x_max) / 2:
            return 2 * (x_max - data) / (x_max - x_min)

    return list(map(normalization, datas))


def datadirection_3(datas, x_min, x_max, x_minimum, x_maximum):  # 区间型->极大型
    def normalization(data):
        if data >= x_min and data <= x_max:
            return 1
        elif data <= x_minimum or data >= x_maximum:
            return 0
        elif data > x_max and data < x_maximum:
            return 1 - (data - x_max) / (x_maximum - x_max)
        elif data < x_min and data > x_minimum:
            return 1 - (x_min - data) / (x_min - x_minimum)

    return list(map(normalization, datas))

# 熵值法
def entropyWeight(data):
    data = np.array(data)
    # 归一化
    P = data / data.sum(axis=0)

    # 计算熵值
    E = np.nansum(-P * np.log(P) / np.log(len(data)), axis=0)

    # 计算权系数
    return (1 - E) / (1 - E).sum()

# TOPSIS方法：输入为数据（已经做好正向化），输出为排名
def topsis(data, weight=None):
    # 归一化
    data = data / np.sqrt((data ** 2).sum())

    # 最优最劣方案
    Z = pd.DataFrame([data.min(), data.max()], index=['负理想解', '正理想解'])

    # 距离
    weight = entropyWeight(data) if weight is None else np.array(weight)
    Result = data.copy()
    Result['正理想解'] = np.sqrt(((data - Z.loc['正理想解']) ** 2 * weight).sum(axis=1))
    Result['负理想解'] = np.sqrt(((data - Z.loc['负理想解']) ** 2 * weight).sum(axis=1))

    # 综合得分指数
    Result['综合得分指数'] = Result['负理想解'] / (Result['负理想解'] + Result['正理想解'])
    Result['排序'] = Result.rank(ascending=False)['综合得分指数']

    return Result, Z, weight
