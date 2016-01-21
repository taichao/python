# coding: utf-8
from snownlp import SnowNLP
a = SnowNLP(u'小妹')
print(a.sentiments)

print(a.sentiments < 0.5)
