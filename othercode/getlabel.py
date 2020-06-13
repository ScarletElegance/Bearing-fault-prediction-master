# -*- coding: UTF-8 -*-
import pandas as pd
import json
import sys, os

res = {}
try:
    # dirs = os.listdir('test2_fea')
    params = {
        'file': 'label/test2.csv',
        'filename':'TEST5'
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
    res['status'] = 0
    df=pd.DataFrame(datacsv)
    index=df[df.filename==params["filename"]].index.tolist()
    res["label"]=df["label"][index].values.tolist()[0]
    # for i in range(len(list(datacsv)) - 1):
    #     data = datacsv.iloc[params['start']:params['end'], i]
    #     res[data.name] = data.values.tolist()
    res['success'] = True
    print(json.dumps(res))
except Exception as e:
    res['msg'] = str(e)
    res['status'] = 1
    res['success'] = False
    print(json.dumps(res))
