import operator

xx = [{'tag': '评审委员会', 'score': 0}, {'tag': '广州', 'score': 2.0027510316}, {'tag': '陈公拓', 'score': 2.0027510316}, {'tag': '郑栩彤', 'score': 4.0027510316}, {'tag': '南方文交所', 'score': 0}]


x = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10},{'name'}]
sorted_x = sorted(xx, key=operator.itemgetter('score'),reverse = True)
print(sorted_x)




