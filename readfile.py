# -*- encoding:utf-8 -*-
import re
import MySQLdb
import datetime

def add_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def add_data(caption,content):
    conn = MySQLdb.Connect(
                            host = '115.29.52.104',
                            port = 3306,
                            user = 'nebula',
                            passwd = '314159',
                            db = 'data',
                            charset = 'utf8'
                            )
    cursor = conn.cursor()
    conn.autocommit(False)

    sql_insert = "insert into shijing(caption,content,add_time) values('"+ caption +"','"+ content +"','"+ add_time() +"')"

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

if __name__ == "__main__":
    f = open("F://shijing.txt")
    list = []
    dict = {}
    #文件读取
    try:
        line = f.readline()
        while  line:
            if (re.match('∷', line)):
                line = re.sub('∷','',line)
                #将标题作为关键字存入list
                key = line
                list.append(key)
                #print key
                line = f.next()
                str = ''
                while (not re.match('∷', line)):
                    #print line
                    str += line
                    line = f.next()
                dict[key] = str
                add_data(key,str)
                continue
            line = f.next()
    except:
        print 'except'
    for key,value in dict.items():
        print key+value
    print  len(list)

    f.close










