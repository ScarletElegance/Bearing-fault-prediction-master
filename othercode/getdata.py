# -*- coding: UTF-8 -*-
import pandas as pd
import json
import sys, os

res = {}
try:
    # dirs = os.listdir('test')
    params = {
        'file': 'train/B01.csv',
        'start': 0,
        'end': -1
    }
    argvs = sys.argv
    for i in range(len(argvs)):
        if i < 1:
            continue
        if argvs[i].split('=')[1] == 'None':
            params[argvs[i].split('=')[0]] = None
        else:
            Type = type(params[argvs[i].split('=')[0]])
            params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])
    datacsv = pd.read_csv(params['file'])
    if (params['end'] == -1):
        params['end'] = len(datacsv)  # 不输入end则获取全部数据
    res['status'] = 0
    res['RPM'] = int(datacsv.iloc[1, -1])
    for i in range(len(list(datacsv)) - 1):
        data = datacsv.iloc[params['start']:params['end'], i]
        res[data.name] = data.values.tolist()
    res['success'] = True
    print(json.dumps(res))
except Exception as e:
    # print(e)
    # res['msg'] = e
    res['status'] = 1
    res['success'] = False
    print(json.dumps(res))
