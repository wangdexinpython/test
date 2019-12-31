# -*- coding: utf-8 -*-
import base64,zlib
ss = '所谓类比法，就是通过选择同类上市公司的一些比率，如最常用的市盈率（P/E即股价/每股收益）、市净率（P/B即股价/每股净资产），再结合新上市公司的财务指标如每股收益、每股净资产来确定上市公司价值，一般都采用预测的指标。'
res = zlib.compress(ss.encode('utf-8'))
print(res)
cons = base64.b64encode(res)
m1 = str(cons,'utf-8')
print(m1)









