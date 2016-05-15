# -*- coding:utf-8 -*-
import smtplib    
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage    
    
sender = 'arvin_fj@163.com'    
receiver = 'arvin_fj@163.com'    
subject = 'MySQL备份'    
smtpserver = 'smtp.163.com'    
username = 'arvin_fj@163.com'    
password = 'flxpdkbukjonbbah'    
    
msgRoot = MIMEMultipart('related')    
msgRoot['Subject'] = 'MySQL备份'
msgRoot['From'] = 'arvin_fj@163.com'
msgRoot['To'] = '594113869@qq.com'
    
#构造附件    
att = MIMEText(open('F:\\ceshi.zip', 'rb').read(), 'base64', 'utf-8')    
att["Content-Type"] = 'application/octet-stream'    
att["Content-Disposition"] = 'attachment; filename="ceshi.zip"'    
msgRoot.attach(att)    
            
smtp = smtplib.SMTP()    
smtp.connect('smtp.163.com')    
smtp.login(username, password)    
smtp.sendmail(sender, receiver, msgRoot.as_string())    
smtp.quit() 
