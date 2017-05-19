# -*- coding: utf-8 -*-

"""
Récupération des informations concernant les foires médiévales
Informations Récupéré sur le site http://www.adagionline.com/calendrier.asp.

    scrapy crawl adagi -o adagi.json
"""

import scrapy
import datetime
from scrapy.loader import ItemLoader
from spiderbox.items import EvenementItem, EvenementLoader
from spiderbox.items import DateItem, DateLoader
from spiderbox.items import DayItem, DayLoader
from spiderbox.items import PictureItem, PictureLoader
from spiderbox.items import AdresseItem, AdresseLoader
from spiderbox.items import ContactItem, ContactLoader
from spiderbox.items import TagItem, TagLoader

class AdagiSpider(scrapy.Spider):

    name = "adagi"
    start_urls = [
            'http://www.adagionline.com/calendrier.asp',
        ]

    def parse(self, response):

        events = []
        now = datetime.datetime.now().isoformat()

        for medieval in response.xpath( '//html/body/table[4]/tr' ):
            event_loader = EvenementLoader( item=EvenementItem(), selector=medieval )
            event_loader.add_xpath( 'title', 'td/font/text()' )
            event_loader.add_value( 'dates', self.get_dates( medieval ) )
            event_loader.add_value( 'pictures', self.get_pictures( medieval ) )
            event_loader.add_value( 'adresses', self.get_adresses( medieval ) )
            event_loader.add_xpath( 'event_url', 'td[3]/font/a/@href' )
            event_loader.add_value( 'registred_by', 'AdagiSpider' )
            event_loader.add_value( 'added_date', now )
            event_loader.add_value( 'contacts', self.get_contacts( medieval ) )
            event_loader.add_value( 'tags', self.get_tags( medieval ) )
            #event_loader.add_value( 'source_url', '' )
#            l.add_value( 'booking_url', site_web )
#            l.add_value( 'contacts', site_web )
#            l.add_value( 'tags', site_web )
#            l.add_value( 'source_url', site_web )
            events.append( event_loader.load_item() )
            break

        return events

#                'site_web' : site_web,
#                'email' : email

    def get_dates( self, medieval ):
        dates_loader = DateLoader( item=DateItem(), selector=medieval )
        dates_loader.add_xpath( 'begin', 'td/font/text()' )
        dates_loader.add_value( 'end', '' )
        dates_loader.add_xpath( 'label', 'td/font/text()' )
        dates_loader.add_value( 'days', self.get_days( medieval ) )
        return dates_loader.load_item()

    def get_days( self, medieval ):
        days_loader = DayLoader( item=DayItem(), selector=medieval )
        days_loader.add_value( 'start', '' )
        days_loader.add_value( 'finish', '' )
        days_loader.add_value( 'price', '' )
        days_loader.add_value( 'comment', '' )
        return days_loader.load_item()

    def get_pictures( self, medieval ):
        pictures_loader = PictureLoader( item=PictureItem(), selector=medieval )
        return pictures_loader.load_item()

    def get_adresses( self, medieval ):
        adresses_loader = AdresseLoader( item=AdresseItem(), selector=medieval )
        adresses_loader.add_xpath( 'pays', 'td[2]/font/img/@src' )
        adresses_loader.add_xpath( 'lieu', 'td/font/a/text()' )
        return adresses_loader.load_item()

    def get_contacts( self, medieval ):
        contacts_loader = ContactLoader( item=ContactItem(), selector=medieval )
        contacts_loader.add_xpath( 'email', 'td[3]/font/a[2]/@href' )
        return contacts_loader.load_item()

    def get_tags( self, medieval ):
        tags_loader = TagLoader( item=TagItem(), selector=medieval )
        return tags_loader.load_item()

    def parse_email( self, selector ):
        """
        Récupération et reforme l'email se trouvant avant ou aprés le site web.
        Note: les cas avec plusieurs sites web puis emails ne sont pas géré.
        """

        email = ''

        # email is after website
        tmp_email = selector.xpath( 'td[3]/font/a[2]/@href' ).extract_first()

        # website doesn't exists so email is first
        if tmp_email is None:
            tmp_email = selector.xpath( 'td[3]/font/a[1]/@href' ).extract_first()

        if tmp_email and '(' in tmp_email:
            tmp_email = tmp_email[tmp_email.index("(") + 1:tmp_email.rindex(")")].split( ',' )
            if len( tmp_email ) == 2:
                email = "%s@%s" % ( tmp_email[1].strip( "'" ), tmp_email[0].strip( "'" ) )
        return email

# TODO
# Ajouter la source ( url;nom;email )
# Ajouter les foires renaissance et celtic
# Le parse du site web et url doit etre revut. Le mail peut etre en 1er position ou 3eme ou neant
# RMQ
# certains loader sont au pluriels alors qu'ils sont utiliser pour fonctionne sur un seul élément.
# Comment serait géré une liste de tags ? un tableau remplit par un loader tag?
