# -*- coding: UTF-8 -*-
import re

corpus = '国务院_ni 总理_n 李克强_nh 调研_v 上海_ns 外高桥_ns 时_n 提出_v'
p = re.compile(r'\_[a-z]+\s?')
news = p.findall(corpus)
print news
print len(news)
print "".join(news)
# print news[6]
# print news[7]



