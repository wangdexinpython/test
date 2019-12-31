import itchat,time
@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print('收到一条消息',msg.text)
if __name__ == '__main__':
    itchat.auto_login()
    time.sleep(5)
    itchat.send('文件助手',toUserName='filehelper')
    itchat.run()