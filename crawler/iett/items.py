# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IettItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LineListingItem(scrapy.Item):
    cdk_id = scrapy.Field()
    name = scrapy.Field()
    node_type = scrapy.Field()
    layer = scrapy.Field()
    code = scrapy.Field()
    clear_name = scrapy.Field()
    type = scrapy.Field()


class StopItem(scrapy.Item):
    layer = scrapy.Field()
    cdk_id = scrapy.Field()
    lat = scrapy.Field() # 41 N
    lon = scrapy.Field() # 29 E
    name = scrapy.Field()
    node_type = scrapy.Field()


class LineDetailItem(scrapy.Item):
    cdk_id = scrapy.Field()
    stop_list = scrapy.Field()
