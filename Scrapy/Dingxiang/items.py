# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingxiangIndexItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    desc = scrapy.Field()
    cover = scrapy.Field()

    def get_insert_sql(self):
        insert_sql='''
        REPLACE INTO `xdl_dx_special_index` (`id`, `name`,`description`, `cover`)
        VALUES (%s, %s, %s, %s)
        '''
        params=(
            self['id'],self['name'],self['desc'],self['cover']
        )
        return insert_sql,params

class DingxiangListItem(scrapy.Item):
    pid = scrapy.Field()
    href_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    imgUrl = scrapy.Field()
    author = scrapy.Field()

    def get_insert_sql(self):
        insert_sql='''
        REPLACE INTO `xdl_dx_special_list` (`pid`, `href_id`, `title`,`description`, `img_url`, `author`)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        params=(
            self['pid'],self['href_id'],self['title'],self['description'],self['imgUrl'],self['author']
        )
        return insert_sql,params

class DingxiangDetailItem(scrapy.Item):
    phref_id = scrapy.Field()
    article = scrapy.Field()
    tags = scrapy.Field()

    def get_insert_sql(self):
        insert_sql='''
        REPLACE INTO `xdl_dx_special_detail` (`pid`, `article`, `tags`)
        VALUES (%s, %s, %s)
        '''
        params=(
            self['phref_id'],self['article'],self['tags']
        )
        return insert_sql,params
