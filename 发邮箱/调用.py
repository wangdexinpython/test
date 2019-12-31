from 发邮箱.youxiang3 import SendEmail


body='邮箱发送。。。'
subject='标题'
try:
    a=[]
    b=a[1]
except Exception as e:
    print(e)
    print(type(e))
    SendEmail(body=str(e),subject='Spider error__query种子获取失败')
    print('ok')
# SendEmail(body=body,subject=subject)
