# -*- encoding:utf-8 -*-
import MySQLdb
import datetime
import jieba

def add_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def select_data(id):
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

    sql_select = "select caption,content from shijing where id=%d" % id

    try:
        cursor.execute(sql_select)
        result = cursor.fetchone()
        conn.commit()
    except Exception as e:
        print e
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
        return result

if __name__ == "__main__":
    jieba.set_dictionary('F://dict.txt')
    jieba.add_word('雎鸠')
    jieba.add_word('好逑')
    #print select_data(1)[1]
    #seg_list = jieba.cut(select_data(1)[1],cut_all=True)
    seg_list = jieba.cut_for_search(select_data(1)[1])
    #print "Full Mode:", "/ ".join(seg_list)  # 全模式
    for i in seg_list:
        print i

