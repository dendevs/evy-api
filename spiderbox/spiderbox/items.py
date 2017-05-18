# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, TakeFirst, MapCompose, Join, Identity
from spiderbox.processors import Ucfirst, TakeNth, TakeSecond, SaveSingle, TakeFirstOrEmptyString


class DayItem( scrapy.Item ):

    start = scrapy.Field()
    finish = scrapy.Field()
    price = scrapy.Field()
    comment = scrapy.Field()

class DateItem( scrapy.Item ):

    begin = scrapy.Field()
    end = scrapy.Field()
    label = scrapy.Field()
    days = scrapy.Field()

class EvenementItem(scrapy.Item):

    title = scrapy.Field()
    description = scrapy.Field()
    website = scrapy.Field()
    dates = scrapy.Field()
    pictures = scrapy.Field()
    adresses = scrapy.Field()
    booking_url = scrapy.Field()
    contacts = scrapy.Field()
    tags = scrapy.Field()
    registred_by = scrapy.Field()
    added_date = scrapy.Field()
    source_url = scrapy.Field()

class EvenementLoader(ItemLoader): # specific adagi

    default_item_class = EvenementItem()
    default_input_processor = Identity()
    default_output_processor = Identity()

    title_in = TakeSecond()
    title_out = SaveSingle()

class DateLoader( ItemLoader ):

    default_item_class = DateItem()
    default_input_processor = Identity()
    default_output_processor = Identity()

    begin_in = TakeFirst()
    begin_out = SaveSingle()

    end_in = Identity()
    end_out = SaveSingle()

    label_in = TakeFirst()
    label_out = SaveSingle()

class DayLoader( ItemLoader ):

    default_item_class = DayItem()
    default_input_processor = Identity()
    default_output_processor = SaveSingle()


# http://stackoverflow.com/questions/25095233/correct-way-to-nest-item-data-in-scrapy
# TODO avoir un fichier pour le model event et n loader prefixer avec le nom du spier  pour remplir le model
