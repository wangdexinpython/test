# -*- coding:utf-8 -*-
import re
title='1'
s1=''
ss = '据外媒路透社报道，日前巴克莱银行和以色列一家初创公司共同完成了全球首个基于区块链技术的贸易交易。通过区块链技术，其在4小时内完成了传统需要耗时7至10日的交易处理流程。该笔贸易结算在巴克莱银行下属的Wave公司开发的区块链平台执行完成，担保了价值约10万美元由爱尔兰Ornua公司向Seychelles Trading Company发货的奶酪和黄油产品。区块链技术相当于一套电子记录和交易处理系统，能够在无需第三方认证的前提下让所有交易参与方在一个安全的网络中跟踪每一笔交易。这种无纸化、去中心化的交易方式比传统笨重的、大量基于纸面文件的交易处理方式更加快捷、更可靠及更容易审计。在过去，这种进出口交易必须通过银行信用证结算，信用证体系相当于国际贸易中的“支付宝”，以第三方的方式保证买卖双方的利益，但是这种体系在实际操作中相当繁琐，需要将出口单据等通过邮寄的方式在进出口双方的银行和客户之间进行传递。除了中途有丢件的风险外，贸易单据造假也时有发生，处理时间上有时可能长达1个月。改用区块链技术后，交易双方将可以通过加密的区块链交换彼此的邮寄、保险和其他原件信息。巴克莱银行全球贸易和营运资本负责人Baihas Baghdadi表示，“我们已经证实了这项技术的可行性。这说明整个流程是十分友好的。”今天区块链技术已被广泛接纳，但很多人认为，该技术仍需要5至10年时间才能普及。不过，鉴于其对银行和贸易公司单证业务人员的替代性，操作性质的单证业务处理岗可或将成为历史。雷锋网原创文章，未经授权禁止转载。详情见转载须知。'
print(ss)
first_word=re.findall('^(.*?)。',s1)
print(first_word)
#
# if 'http' in title or title=='':
#     print('22222')






