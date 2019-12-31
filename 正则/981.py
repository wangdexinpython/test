import re
# ss="我手机号151070103269"
ss = '我手机号15107103269'
# re_cell=re.compile(r"(?:^|\D)(1[3|4|5|6|7|8|9][0-9]\d{8})(?:$|\D)")
re_cell = re.compile(r"(?:^|\D)(1[3|4|5|6|7|8|9][0-9]\d{8})(?:$|\D)")

print(re_cell.findall(ss))
# cell_items=[]
# cell_spans=[]
# for cell in re_cell.finditer(ss):
#     print(cell.group())
#     cell_items.append(cell.group())
# print(cell_items)
# print(cell_spans)
import re
s = "我手机号15107103269"
re_cell = re.compile(r"(?:^|\D)(1[3|4|5|6|7|8|9][0-9]\d{8})(?:$|\D)")
print(re_cell.findall(s))

for cell in re_cell.finditer(s):
    print(cell.group())
