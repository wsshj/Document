import numpy as np
import pandas as pd
import os
import json

#写
writer = pd.ExcelWriter('部门.xlsx')
for i in range(10):
    dic = {'级别': ['','张三','李四'],
            '序号': ['',80, 90],
            '工作项目': ['',80, 90],
            '工作任务': ['',80, 90],
            '工作内容': ['',80, 90],
            '完成情况': ['',80, 90],
            '开始时间': ['',80, 90],
            '累计工时': ['',80, 90],
            '备  注': ['',80, 90]
    }
    df = pd.DataFrame(dic)
    df.to_excel(writer, sheet_name='%s' % i, index=False)

writer.save()