# -*- coding:utf-8 -*-
#!/usr/bin/python
import json
import urllib
import urllib2
import datetime
import MySQLdb

def insert_mysql(content):
    conn = MySQLdb.Connect(
                            host = '115.29.52.104',
                            port = 3306,
                            user = 'nebula',
                            passwd = '314159',
                            db = 'one',
                            charset = 'utf8'
                            )
    cursor = conn.cursor()

    # 获取时间
    now = datetime.datetime.now()
    now_strf = now.strftime("%Y-%m-%d %H:%M:%S")
    print now_strf

    sql_insert = "insert into joke (content,add_time) values('"+ content +"','"+now_strf +"')"
    #print sql_insert
    try:
        cursor.execute(sql_insert)
        print cursor.rowcount
        conn.commit()
    except Exception as e:
        print e
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def joke():
    url = "http://www.tuling123.com/openapi/api"
    data = {'key':'72307a3ae94c424381b2a023a9df3520','info':'讲个笑话'}
    data_urlencode = urllib.urlencode(data)
    req = urllib2.Request(url = url,data =data_urlencode)
    #print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    s = json.loads(res)
    #print res
    insert_mysql(s["text"])

if __name__ == "__main__":
    joke()
