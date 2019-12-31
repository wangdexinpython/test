import time
filename = time.strftime("%Y%m%d", time.localtime())
scp_time = int(time.strftime("%Y%m%d%H%M%S", time.localtime()))
# fi = 230001
# if scp_time>fi:
#     print("0000")
print('scp',scp_time)
fi = time.strftime("%M%S", time.localtime())
print(fi)



