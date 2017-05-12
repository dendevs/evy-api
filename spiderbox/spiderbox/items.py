# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, TakeFirst, MapCompose, Join, Identity
from spiderbox.processors import Ucfirst

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


class EvenementLoader(ItemLoader): # specific adagi

    #default_output_processor = Identity()

    title_in = TakeFirst()
    #title_out = Compose(lambda v: v[0], )
    title_out = Ucfirst() # TODO take nth ( 2 ), Ucfirst, display accents

    #title_in = TakeFirst()
    #title_out = MapCompose(unicode.strip)
