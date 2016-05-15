# -*- encoding:utf-8 -*-
import MySQLdb
import datetime

#获取当前时间
def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

#读取daily_sentence.txt文件内容
def read_daily_sentence():
    f = open("daily_sentence.txt")
    #文件读取
    str = f.read()
    f.close
    return str



print read_daily_sentence()


def mysql_operate():
    conn = MySQLdb.Connect(
                        host = '115.29.52.104',
                        port = 3306,
                        user = 'nebula',
                        passwd = '314159',
                        db = 'one',
                        charset = 'utf8'
                        )
    cursor = conn.cursor()
    #conn.autocommit(False)
    sql_insert = "insert into daily_sentence(sentence,add_time) values('"+ read_daily_sentence() +"','"+ get_current_time() +"')"
    print sql_insert
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

mysql_operate()


