# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DayItem( scrapy.Item ):
    startAt = scrapy.Field()
    finishAt = scrapy.Field()
    price = scrapy.Field()
    comment = scrapy.Field()

class DatesItem( scrapy.Item):
    begin_date = scrapy.Field()
    end_date = scrapy.Field()
    days = DayItem()

class EvenementItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    website = scrapy.Field()
    dates = DatesItem()
    pictures = scrapy.Field()
    adresses = scrapy.Field()
    booking_url = scrapy.Field()
    contacts = scrapy.Field()
    tags = scrapy.Field()
    registred_by = scrapy.Field()
    added_date = scrapy.Field()
    source_url = scrapy.Field()
