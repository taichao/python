# coding: utf-8
from snownlp import SnowNLP
a = SnowNLP(u'墨头号毒枭逃亡期间密会zhong国老牌影帝')
print(len(u'人民币对美元汇率中间价继续下跌10个基点(2014-12-23 10:23:06)_...'))
b = a.sim(u'人社部要求停发美甲师职业资格证|美甲师|人社部_新浪财经_新浪网')
print(b)
