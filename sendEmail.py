
#!/usr/bin/env python3
# coding=utf-8

# sendEmail title content
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'liuhao@yueke100.net;'
receiver = 'hao1iu@126.com;hao1iu@qq.com;'
smtpserver = 'smtp.mxhichina.com'

username = 'liuhao@yueke100.net'
password = 'LXQ.com.123'

def send_mail(title, content):
    
    try:
        msg = MIMEText(content,'plain','utf-8')
        if not isinstance(title,unicode):
            title = unicode(title, 'utf-8')
        msg['Subject'] = title
        msg['From'] = sender
        msg['To'] = receiver
        msg["Accept-Language"]="zh-CN"
        msg["Accept-Charset"]="ISO-8859-1,utf-8"

        smtp = smtplib.SMTP_SSL(smtpserver,465)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        return True
    except Exception, e:
        print str(e)
        return False

if send_mail(sys.argv[1], sys.argv[2]):
    print "done!"
else:
    print "failed!"
