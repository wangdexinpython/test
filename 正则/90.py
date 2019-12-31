import re
ss='时间大于三天'
cons=re.findall(r'(?:大于|小于)?([三])',ss)
con=re.findall(r'(?:大于|小于)',ss)

print(cons)
print(con)