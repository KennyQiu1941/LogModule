import zmail
from setting import Email

def sender(msg):
    '''读取配置文件发送邮件'''
    server = zmail.server(Email.username, Email.password)
    mail = {
        'from': '服务器消息推送',
        'subject': '',
        'content_text': msg,
    }
    try:
        server.send_mail(Email.target_email_addr, mail)
    except Exception as e:
        print('发送失败')
    else:
        print('成功发送邮件')
