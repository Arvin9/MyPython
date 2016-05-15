# -*- encoding:utf-8 -*-
import time
import urllib2
import urllib
import thread 
from random import Random

def random_str(randomlength=3):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def random_num(randomlength=9):
    str = '13'
    chars = '1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


#print random_str()

#   2116871   2116887

def post_data(id):
    #����һ��Ҫ�ύ����������(�ֵ�)
    data = {}
    data['jq[]'] = id
    data['name'] = random_str()
    data['tel'] = random_num()

    print 
    print 'id:'+id
    print 'name:'+data['name']
    print 'tel:'+data['tel']
     
    #����post�ĵ�ַ
    url = 'http://new.wehefei.com/htmlphp/szddg2016/ask11.php?act=add'
    post_data = urllib.urlencode(data)
     
    #�ύ����������
    req = urllib2.urlopen(url, post_data)
     
    #��ȡ�ύ�󷵻ص���Ϣ
    content = req.read()

    print 
    print content


def vote(id,star,end):
    for i in range(1,1000):
        post_data(id)
        #time.sleep(Random().randint(star,end))

def test_thread():
    thread.start_new_thread(vote, ('2116871',2,4))
    thread.start_new_thread(vote, ('2116887',1,3))

test_thread()

