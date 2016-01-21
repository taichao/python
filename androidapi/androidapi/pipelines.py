# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os,urlparse
from scrapy.exceptions import DropItem

class AndroidapiPipeline(object):

    htmlpath = "/Users/zhangtaichao/code/python/androidapi/html"

    def process_item(self, item, spider):
        if 'url' not in item:
            raise DropItem()
        url = item.get('url')
        url = urlparse.urlparse(url)

        p = os.path.join(self.htmlpath,url.path[1:])
        sp = os.path.split(p)
        if not os.path.exists(sp[0]):
            os.makedirs(sp[0])
        with open(p,'w') as f:
            f.write(item['content'].encode('utf-8'))
        return item
