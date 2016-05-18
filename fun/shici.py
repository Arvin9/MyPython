# -*- coding: utf-8 -*-
#爬取http://www.shi-ci.com/每日精选内容
#存入数据库
import requests
import bs4
import datetime
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def insert_mysql(caption,derivation,content,appraisal):
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

    sql_insert = "insert into shici (caption,derivation,content,appraisal,add_time) values('"+ caption +"','"+ derivation +"','"+ content +"','"+appraisal +"','"+now_strf +"')"
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


def shici():
    # 爬取内容
    response = requests.get('http://www.shi-ci.com/')
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    for i in soup.find_all("div", class_="poem-read"):
        # 获取标题
        caption = i.find_all('p')[1].string
        print caption
        # 获取出处
        derivation = i.find_all('p')[2].find_all('a')[0].string +u'·'+ i.find_all('p')[2].find_all('a')[1].string
        print derivation
        # 获取句子
        content = i.find_all('p')[3].string
        print content

    appr = soup.find_all("div", class_="poem-appr")[0].find_all('p')[1].string
    print appr
    insert_mysql(caption,derivation,content,appr)

if __name__ == "__main__":
    shici()