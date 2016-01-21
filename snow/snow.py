# coding: utf-8
from snownlp import SnowNLP,tag
import os.path
base = os.path.dirname(__file__)
tagsrc = os.path.join(base,'model/tag/199801.txt')
tagdest = os.path.join(base,'model/tag/tag.marshal')
tag.train(tagsrc)
tag.save(tagdest)

