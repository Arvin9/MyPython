# -*- coding: utf-8 -*-
#读取数据库中诗经
#将读取内容发送至邮箱
import MySQLdb
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def select_mysql():
    conn = MySQLdb.Connect(
                            host = '115.29.52.104',
                            port = 3306,
                            user = 'nebula',
                            passwd = '314159',
                            db = 'data',
                            charset = 'utf8'
                            )
    cursor = conn.cursor()

    sql_select = "select id,caption,content from shijing order by times limit 1"

    try:
        cursor.execute(sql_select)
        #print cursor.rowcount
        results = cursor.fetchall()
        conn.commit()
    except Exception as e:
        print e
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    return results

def update_mysql(id):
    conn = MySQLdb.Connect(
                            host = '115.29.52.104',
                            port = 3306,
                            user = 'nebula',
                            passwd = '314159',
                            db = 'data',
                            charset = 'utf8'
                            )
    cursor = conn.cursor()
    sql_update = "update shijing set times=times+1 where id=%d" % id
    try:
        cursor.execute(sql_update)
        print cursor.rowcount
        conn.commit()
    except Exception as e:
        print e
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def mysendmail(caption,content):
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
    subject=u'诗经'
    msgText="<html><p><h2>%s</h2>%s</p></html>" % (caption,content)


    msg = MIMEText(msgText, 'html', 'utf-8')
    msg['From'] = _format_addr(addresser % from_mail)
    msg['To'] = _format_addr(recipient % to_mail)
    msg['Subject'] = Header(subject, 'utf-8').encode()

    server.docmd('ehlo','arvin_fj@163.com')
    server.login('arvin_fj@163.com','flxpdkbukjonbbah')
    server.sendmail(from_mail,to_mail,msg.as_string())
    server.quit()

if __name__ == "__main__":
    for row in select_mysql():
        id = row[0]
        caption = row[1]
        content = row[2]
    print id
    print caption
    content = '<h3>'+content.replace('。','。</h3><h3>')+'</h3>'
    print content
    update_mysql(id)
    mysendmail(caption,content)
