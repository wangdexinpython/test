import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
class SendEmail(object):
    def __init__(,**kwargs):
        email_host = 'smtp.163.com'
        email_port = '465'
        email_sender = 'w18310761194@163.com'
        email_receiver = '1253949887@qq.com'
        email_password = 'jiexin88'
        # 发送纯文本邮件
        body=kwargs.get('body')
        subject=kwargs.get('subject')
        run()
    def send_text_email(, body,subject):
        # 1.内容主体
        # 2.内容类型
        # 3.编码方式
        message_text = MIMEText(body, 'plain', 'utf-8')
        message_text['From'] = email_sender
        message_text['To'] = email_receiver
        message_text['Subject'] = subject
        try:
            email_client = smtplib.SMTP_SSL(email_host, email_port)
            login_result = email_client.login(email_sender, email_password)
            print('开始登录', login_result)
            # 如果有登录信息 而且登录信息里面第一条状态码为235说明登陆成功
            if login_result and login_result[0] == 235:
                print('登录成功')
                email_client.sendmail(email_sender, email_receiver, message_text.as_string())
                print('发送完成')
            else:
                print('登录失败')
        except Exception as e:
            print('邮件发送失败', e)
    def run():
        send_text_email(body,subject)



