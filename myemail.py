# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

from_mail='arvin_fj@163.com'
to_mail='594113869@qq.com'
server=smtplib.SMTP('smtp.163.com')

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))



addresser=u'Nebula <%s>'
recipient=u'qcloud <%s>'
subject=u'来自Nebula的问候'
msgText='hello, send by Python'


msg = MIMEText(msgText, 'plain', 'utf-8')
msg['From'] = _format_addr(addresser % from_mail)
msg['To'] = _format_addr(recipient % to_mail)
msg['Subject'] = Header(subject, 'utf-8').encode()


server.docmd('ehlo','arvin_fj@163.com')
server.login('arvin_fj@163.com','flxpdkbukjonbbah')
server.sendmail(from_mail,to_mail,msg.as_string())
server.quit()
  
