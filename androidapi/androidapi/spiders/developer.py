# -*- coding: utf-8 -*-
import scrapy
from androidapi.items import HtmlItem


class DeveloperSpider(scrapy.Spider):
    name = "developer"
    urlset = set()
    allowed_domains = ["android.com"]
    start_urls = (
        'http://developer.android.com/develop/index.html',
    )

    def parse(self, response):
        item = HtmlItem()
        item['url'] = response.url
        item['content'] = response.body_as_unicode()
        yield item

        sel = response.css('.dac-nav-secondary .dac-nav-item .dac-nav-link[href]')
        hrefs = sel.css('::attr(href)')
        for i in hrefs:
            href = i.extract()
            url = response.urljoin(href)
            if url not in self.urlset:
                self.urlset.add(url)
                print(url)
                yield scrapy.Request(url,self.parseHtml)
        self.parseother(response)

    def parseHtml(self,response):
        item = HtmlItem()
        url = response.url
        if '?' in url:
            url = url[0:url.find('?')]
        item['url'] = url
        item['content'] = response.body_as_unicode()
        yield item
        self.parseother(response)
        sel = response.css('#devdoc-nav a::attr(href)')
        sels = response.css('#side-nav a::attr(href)')
        sel.extend(sels)
        for i in sel:
            href = i.extract()
            url = response.urljoin(href)
            if url not in self.urlset:
                self.urlset.add(url)
                print(url)
                yield scrapy.Request(url,self.parseHtml)



    def parseother(self,response):
        jss = response.xpath('//script/@src')
        for i in jss:
            i = i.extract()
            if '/' == i[0] and '/' != i[1]:
                url = response.urljoin(i)
                if url not in self.urlset:
                    self.urlset.add(url)
                    yield scrapy.Request(url,self.parseHtml)

        css = response.xpath('//link/@href')
        for i in css:
            i = i.extract()
            if '/' == i[0] and '/' != i[1]:
                url = response.urljoin(i)
                if url not in self.urlset:
                    self.urlset.add(url)
                    print(url)
                    yield scrapy.Request(url,self.parseHtml)


