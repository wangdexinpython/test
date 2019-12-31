
path='G:\合作数据\zhidao_statistics (2).txt'
num1=0
with open(path,'r',encoding='utf-8') as f:
    ss = f.readlines()
    for s in ss:
        s1 = s.replace('\n','')
        li1 = s1.split('_')
        num1 += int(li1[3])
        print(num1)







