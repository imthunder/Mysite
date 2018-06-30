# -*- coding: utf-8 -*-
import scrapy
from Dingxiang.items import DingxiangIndexItem, DingxiangListItem, DingxiangDetailItem
from scrapy import Request
import json
import re
from bs4 import BeautifulSoup

class DingxiangSpider(scrapy.Spider):
    name = 'dingxiang'
    allowed_domains = ['https://dxy.com']
    baseIndexUrl = 'https://dxy.com/view/i/columns/special/list?page_index={}&items_per_page=12'
    indexPage = 1
    baseListUrl = 'https://dxy.com/column/special/{}/'
    detailUrl = 'https://dxy.com/column/{}'
    start_urls = [baseIndexUrl.format(indexPage)]

    def parse(self, response):
        result = json.loads(response.text)
        items = result['data']['items']
        totalPage = result['data']['total_pages']
        for item in items:
            dxItem = DingxiangIndexItem()
            dxItem['id'] = item['id']
            dxItem['name'] = item['name']
            dxItem['desc'] = item['desc']
            dxItem['cover'] = self.addHttp(item['cover'])
            yield dxItem
            yield Request(self.baseListUrl.format(item['id']), callback=self.parseList, dont_filter=True)

        if int(totalPage) == self.indexPage:
            return
        self.indexPage += 1
        yield Request(self.baseIndexUrl.format(self.indexPage), callback=self.parse, dont_filter=True)

    def parseList(self, response):
        table = response.xpath('//dl')
        for cell in table:
            item = DingxiangListItem()
            item['pid'] = re.findall(r'\d+',response.url)[0]
            hrefUrl = cell.xpath('dt/a/@href')[0].extract()
            item['href_id'] = re.findall(r'\d+',hrefUrl)[0]
            item['title'] = cell.xpath('dd//h4/a/text()')[0].extract()
            item['author'] = cell.xpath('dd//div[@class="author"]/a/text()')[0].extract()
            item['description'] = cell.xpath('dd/div[@class="description"]/text()')[0].extract()
            item['imgUrl'] = self.addHttp(cell.xpath('dt//img/@src')[0].extract())
            yield item
            yield Request(self.detailUrl.format(item['href_id']), callback=self.parseDetail, dont_filter=True)

    def parseDetail(self, response):
        item = DingxiangDetailItem()
        item['phref_id'] = re.findall(r'\d+',response.url)[0]
        item['tags'] = ','.join(response.xpath('//a[@class="tag-item"]/text()').extract())
        item['article'] = response.xpath('//div[@class="pg-article-inner"]')[0].extract()
        soup = BeautifulSoup(item['article'])
        del_node = soup.find('strong')
        if del_node:
            del_node.decompose()

        divs = ['mod-tag','like-box','pg-share-box','col-pager-relate']
        for div in divs:
            del_div = soup.find('div',{'class': div})
            if del_div:
                del_div.decompose()
        item['article'] = str(soup.body.div)
        yield item


    def addHttp(self, cover):
        if cover[0:2] == '//':
            cover = 'http:' + cover
        return cover
