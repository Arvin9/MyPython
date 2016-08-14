#!/usr/bin/python
# -*- coding: utf-8 -*- #

import datetime
import jieba
import MySQLdb
import codecs
import uuid
import paramiko
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class Sentence2wordcloud:
    #类变量，它的值将在这个类的所有实例之间共享。

    def __init__(self):
        self.conn = MySQLdb.Connect(
            host = '115.159.86.92',
            port = 3306,
            user = 'community',
            passwd = 'community',
            db = 'community',
            charset = 'utf8'
        )
    # 查询sentence数据
    def select_mysql(self,id):
        print 'start select sentence ...'
        cursor = self.conn.cursor()
        # 获取时间
        #now = datetime.datetime.now()
        #now_strf = now.strftime("%Y-%m-%d %H:%M:%S")
        #print now_strf
        sql_select = "select daily_sentence_id,daily_sentence from daily_sentence where daily_sentence_id = %d " % id
        try:
            cursor.execute(sql_select)
            result = cursor.fetchone()
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()
            print 'select sentence done...'
            return result

    # 对sentence进行分词
    # 输入sentence返回元组列表
    # 逗号，等一些词需去掉
    def sentence_jieba(self,sentence):
        print 'start jieba ...'
        # 停止词
        stop_word = ([line.rstrip() for line in codecs.open('D:/stop_words.txt', 'r', 'UTF-8')])
        result = {} # 带词频的字典
        seg_list = jieba.cut_for_search(sentence)  # 搜索引擎模式
        new_list = []
        for seg in seg_list:
            if seg not in stop_word:
                new_list.append(seg)
        for word in new_list:
            result[word] = result.get(word, 0) + 1
        list = [] # 元组列表
        for k in result.keys():
            tu = (k,result[k])
            list.append(tu)
        # print list
        return list
        print 'jieba done'

    # 对分词好的sentence画云词
    def sentence_wordcloud(self,frequencies,local_url):
        print 'start wordcloud ...'
        #frequencies = [(u'中文', 1), (u'你好', 1), (u'在吗', 1), (u'在哪', 1), (u'什么', 1)]
        wordcloud = WordCloud(max_font_size=200, relative_scaling=.5).fit_words(frequencies)
        plt.figure()
        plt.imshow(wordcloud)
        plt.axis("off")

        plt.savefig(local_url)
        #plt.show()
        print 'wordcloud done'

    # 上传云词到http://image.nebulas.site/image/
    def upload_wordcloud(self,localpath,img_uuid):
        print 'start upload_wordcloud ...'
        my_host = "115.29.52.104"
        my_username = "root"
        my_password = "CHh314159"
        t = paramiko.Transport((my_host, 22))
        t.connect(username=my_username, password=my_password)
        sftp = paramiko.SFTPClient.from_transport(t)
        # /usr/share/tomcat/webapps
        remotepath = '/var/www/html/image/%s.jpg' % img_uuid
        #localpath = 'C:/Users/Administrator/Desktop/' + filename
        sftp.put(localpath, remotepath)
        t.close()
        print 'upload_wordcloud done'

    # 将图片的url写入数据库
    # 可用
    def update_sentence(self,id,url):
        print 'start update sentence ...'
        cursor = self.conn.cursor()
        sql_update = "update daily_sentence set daily_sentence_url='%s' where daily_sentence_id=%d" % (url,id)
        try:
            cursor.execute(sql_update)
            print cursor.rowcount
            self.conn.commit()
        except Exception as e:
            print e
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()
        print 'update_sentence done'

    def get_uuid(self):
        return str(uuid.uuid4()).replace('-', '')
        # 输出: d5b853fd918442f5af7038b5c7410cb1

if __name__ == "__main__":
    for id in range(1,213):
       #获取uuid,确定路径
        sw = Sentence2wordcloud()
        img_uuid = sw.get_uuid()
        local_url = 'D:/image/%s.png' % img_uuid
        aliyun_url = 'http://image.nebulas.site/image/%s.jpg' % img_uuid
       # 根据获取sentence数据
        sw = Sentence2wordcloud()
        sentence = sw.select_mysql(id)[1]  # 由id获得sentence
        print sentence
       # 对sentence进行分词
        sw = Sentence2wordcloud()
        list_tuple = sw.sentence_jieba(sentence)
        print list_tuple
        # 对分词好的sentence画云词
        sw = Sentence2wordcloud()
        sw.sentence_wordcloud(list_tuple,local_url)


        # 上传云词到http://image.nebulas.site/image/
        sw = Sentence2wordcloud()
        sw.upload_wordcloud(local_url,img_uuid)
        print local_url
        print aliyun_url
        # 将图片的url写入数据库
        sw = Sentence2wordcloud()
        sw.update_sentence(id,aliyun_url)
