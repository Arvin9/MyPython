# -*- coding: utf-8 -*- 
# Pyrhon生成唯一标识符（字符串形式）
import uuid  
  
  
print str(uuid.uuid4())  
# 输出: daf577eb-5874-41f4-8b35-0debe1f86180  
# or   
print str(uuid.uuid4()).replace('-', '')  
# 输出: d5b853fd918442f5af7038b5c7410cb1  
