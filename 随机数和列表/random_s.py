
# import random
# # random.choice(range(1,34))
# # s1 = random.choices(range(1,9),k=6,weights=range(1,9))
# s1 = random.sample(range(0,8),6)
# print(s1)
#
# li=[1,2]
# print(li)
# li.reverse()
# print(li)

import operator

x = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':340}]
sorted_x = sorted(x, key=operator.itemgetter('age'),reverse=True)


print(sorted_x)







