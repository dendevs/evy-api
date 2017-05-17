# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, TakeFirst, MapCompose, Join, Identity
from spiderbox.processors import Ucfirst, TakeNth, TakeSecond, SaveSingle, TakeDates, SaveDates


class DayItem( scrapy.Item ):

    startAt = scrapy.Field()
    finishAt = scrapy.Field()
    price = scrapy.Field()
    comment = scrapy.Field()

class DatesItem( scrapy.Item ):

    begin_date = scrapy.Field()
    end_date = scrapy.Field()
    #days = scrapy.Field( serializer=DayItem )
    #days = scrapy.Field( )
    pass

class EvenementItem(scrapy.Item):

    title = scrapy.Field()
    description = scrapy.Field()
    website = scrapy.Field()
    #dates = scrapy.Field( serializer=DatesItem )
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

    #dates_in = TakeDates()
    #dates_out = SaveDates()

class DatesLoader( ItemLoader ):

    default_item_class = DatesItem()
    default_input_processor = Identity()
    default_output_processor = Identity()

    begin_date_in = TakeFirst()
    begin_date_out = SaveSingle()

    end_date_in = TakeFirst()
    end_date_out = SaveSingle()

class DayItem( ItemLoader ):

    default_item_class = DayItem()
    default_input_processor = Identity()
    default_output_processor = Identity()




# http://stackoverflow.com/questions/25095233/correct-way-to-nest-item-data-in-scrapy
# TODO avoir un fichier pour le model event et n loader prefixer avec le nom du spier  pour remplir le model
