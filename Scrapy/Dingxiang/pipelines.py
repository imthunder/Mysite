# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import DingxiangDetailItem, DingxiangListItem, DingxiangIndexItem
import pymysql
import pymysql.cursors
from twisted.enterprise import adbapi

class DingxiangPipeline(object):

    def __init__(self,dbpool):
        self.dbpool=dbpool
    @classmethod
    def from_settings(cls,settings):
        dbpool=adbapi.ConnectionPool("pymysql",host=settings["MYSQL_HOSTS"],db=settings["MYSQL_DB"],port=settings["MYSQL_PORT"],user=settings["MYSQL_USER"],password=settings["MYSQL_PASSWORD"],charset="utf8", cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True)
        return cls(dbpool)

    def process_item(self,item,spider):
        # 使用twisted将mysql插入变成异步执行
        self.dbpool.runInteraction(self.do_insert,item)


    def do_insert(self,cursor,item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)
