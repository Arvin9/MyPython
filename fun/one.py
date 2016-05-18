# -*- coding: utf-8 -*- #
import requests
import bs4
import re
import datetime
import MySQLdb
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

def mysendmail(img_src,a_content):
    from_mail='arvin_fj@163.com'
    to_mail='594113869@qq.com'
    server=smtplib.SMTP('smtp.163.com')

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))



    addresser=u'Nebula<%s>'
    recipient=u'qcloud <%s>'
    subject=u'来自Nebula的问候'
    msgText='<html><p><img width="350" height="400" src="'+img_src+'" /></p><h3>'+a_content+'</h3></html>'


    msg = MIMEText(msgText, 'html', 'utf-8')
    msg['From'] = _format_addr(addresser % from_mail)
    msg['To'] = _format_addr(recipient % to_mail)
    msg['Subject'] = Header(subject, 'utf-8').encode()


    server.docmd('ehlo','arvin_fj@163.com')
    server.login('arvin_fj@163.com','flxpdkbukjonbbah')
    server.sendmail(from_mail,to_mail,msg.as_string())
    server.quit()
    


#打开数据库连接
conn = MySQLdb.Connect(
                        host = '115.29.52.104',
                        port = 3306,
                        user = 'nebula',
                        passwd = '314159',
                        db = 'one',
                        charset = 'utf8'
                        )
cursor = conn.cursor()
conn.autocommit(False)

#爬取内容
response = requests.get('http://wufazhuce.com')
soup = bs4.BeautifulSoup(response.text,"html.parser")



for i in soup.find_all("div",class_="item active"):
    #获取图片连接
    img_src = i.find_all('img')[0]['src']
    print img_src
    #获取句子
    a_content = i.find_all('a')[1].string
    print a_content

#获取时间
now = datetime.datetime.now()
now_strf = now.strftime("%Y-%m-%d %H:%M:%S")
print now_strf

mysendmail(img_src,a_content)

"""
#写入数据库      
sql_insert_img_src = "insert into image_links(link,add_time) values('" + img_src + "','" + now_strf + "')"
sql_insert_a_content = "insert into quotations(content,add_time) values('" + a_content + "','" + now_strf + "')"

print sql_insert_img_src
print sql_insert_a_content

try:
    cursor.execute(sql_insert_img_src)
    print cursor.rowcount

    cursor.execute(sql_insert_a_content)
    print cursor.rowcount

    conn.commit()
except Exception as e:
    print e
    conn.rollback()
finally:
    cursor.close()
    conn.close()

"""


