import smtplib
import logging

class EmailSend():
    def __init__():
        pass
    def send_text_email(,from_addr,to_addrs,subject,content):
        # 网易163邮箱
        HOST = 'smtp.exmail.qq.com'
        # 2> 配置服务的端口，默认的邮件端口是25.
        PORT = '465'
        # 创建邮件发送对象
        # 普通的邮件发送形式
        smtp_obj = smtplib.SMTP()

        # 需要进行发件人的认证，授权。
        # smtp_obj就是一个第三方客户端对象
        smtp_obj.connect(host=HOST, port=PORT)

        # 如果使用第三方客户端登录，要求使用授权码，不能使用真实密码，防止密码泄露。
        res = smtp_obj.login(user=from_addr, password='jiexin8888')
        print('登录结果：', res)

        # 发送邮件
        msg = '\n'.join(['From: {}'.format(from_addr), 'To: {}'.format(to_addrs), 'Subject: {}'.format(subject), '', content])
        smtp_obj.sendmail(from_addr=from_addr, to_addrs=to_addrs, msg=msg.encode('utf-8'))

if __name__ == '__main__':
    Spider = EmailSend()
    from_addr = 'w18310761194@163.com'
    to_addrs = 'wangdexin@haxitag.com'
    subject = 'Spider报警系统'
    content = 'Hello!'
    Spider.send_text_email(from_addr,to_addrs,subject,content)

    