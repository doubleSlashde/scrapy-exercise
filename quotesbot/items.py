# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesbotItem(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()
    author_forename = scrapy.Field()
    author_surname = scrapy.Field()
    pass
