# -*- coding:utf-8 -*-
"""
作者：段晓晨
链接：http://zhuanlan.zhihu.com/p/20436642
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
# 此处原为处理英文文本，我们修改为传入中文数组
#text = open(path.join(d, 'constitution.txt')).read()
frequencies = [(u'知乎',5),(u'小段同学',4),(u'曲小花',3),(u'中文分词',2),(u'样例',1)]

# Generate a word cloud image 此处原为 text 方法，我们改用 frequencies 
#wordcloud = WordCloud().generate(text)
wordcloud = WordCloud().fit_words(frequencies)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# take relative word frequencies into account, lower max_font_size
#wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).fit_words(frequencies)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
#image = wordcloud.to_image()
#image.show()
