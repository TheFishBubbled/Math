import TOPSIS
import pandas as pd

data = pd.DataFrame(
    {'人均专著': [0.1, 0.2, 0.4, 0.9, 1.2], '生师比': [5, 6, 7, 10, 2], '科研经费': [5000, 6000, 7000, 10000, 400],
     '逾期毕业率': [4.7, 5.6, 6.7, 2.3, 1.8]}, index=['院校' + i for i in list('ABCDE')])

data['生师比'] = TOPSIS.datadirection_3(data['生师比'], 5, 6, 2, 12)   # 师生比数据为区间型指标
data['逾期毕业率'] = 1 / data['逾期毕业率']   # 逾期毕业率为极小型指标

out = TOPSIS.topsis(data, weight=[0.2, 0.3, 0.4, 0.1])    # 设置权系数
print(out)