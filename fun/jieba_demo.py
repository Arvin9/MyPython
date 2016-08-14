# -*- coding: utf-8 -*-


import jieba
import sys
import codecs
'''
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print "Full Mode:", "/ ".join(seg_list)  # 全模式
 
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print "Default Mode:", "/ ".join(seg_list)  # 精确模式
 
seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print ", ".join(seg_list)
'''
seg_list = jieba.cut_for_search("小明的硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式

#stop_word =[u'的',u'于',u'，']
stop_word = ([ line.rstrip() for line in codecs.open('D:/stop_words.txt','r','UTF-8') ])
print stop_word

for seg in seg_list:
    if seg not in stop_word:
        print seg

print ", ".join(seg_list)
