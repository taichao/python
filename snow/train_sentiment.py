# coding: utf-8
from snownlp import SnowNLP,sentiment
import os.path
base = os.path.dirname(__file__)
pos = os.path.join(base,'model/sentiment/pos.txt')
neg = os.path.join(base,'model/sentiment/neg.txt')
tagdest = os.path.join(base,'model/sentiment/sentiment.marshal')
sentiment.train(neg,pos)
sentiment.save(tagdest)

