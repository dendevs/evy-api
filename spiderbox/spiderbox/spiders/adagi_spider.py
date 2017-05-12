# -*- coding: utf-8 -*-

"""
Récupération des informations concernant les foires médiévales
Informations Récupéré sur le site http://www.adagionline.com/calendrier.asp.

    scrapy crawl adagi -o adagi.json
"""

import scrapy
from scrapy.loader import ItemLoader
from spiderbox.items import EvenementItem, EvenementLoader

class AdagiSpider(scrapy.Spider):

    name = "adagi"
    start_urls = [
            'http://www.adagionline.com/calendrier.asp',
        ]

    def parse(self, response):

        print 'Response'
        print response
        events = []

        for medieval in response.xpath( '//html/body/table[4]/tr' ):
            print 'selector'
            print medieval
            event_loader = EvenementLoader( item=EvenementItem(), selector=medieval )
            event_loader.add_xpath( 'title', 'td/font/text()' )
#            l.add_value( 'dates', site_web )
#            l.add_value( 'pictures', None )
#            l.add_value( 'adresses', site_web )
#            l.add_value( 'booking_url', site_web )
#            l.add_value( 'contacts', site_web )
#            l.add_value( 'tags', site_web )
#            l.add_value( 'registred_by', site_web )
#            l.add_value( 'added_date', site_web )
#            l.add_value( 'source_url', site_web )
            events.append( event_loader.load_item() )
            break

        return event_loader.load_item()

#                'dates' : medieval.xpath( 'td/font/text()' ).extract_first(),
#                'pays' : pays,
#                'lieu' : medieval.xpath( 'td/font/a/text()' ).extract_first(),
#                'titre' : medieval.xpath( 'td/font/text()' ).extract_first(),
#                'site_web' : site_web,
#                'email' : email

    def parse_pays( self, selector ):
        """
        Transforme l'image drapeau en une valeur fr,be,... désignant le pays
        """

        pays = ''
        tmp_pays = selector.xpath( 'td[2]/font/img/@src' ).extract_first()

        if tmp_pays:
            tmp_pays = tmp_pays.split( "/" )
            if tmp_pays:
                pays = tmp_pays[1].split( '.' )[0]

        return pays

    def parse_site_web( self, selector ):
        """
        Récupére l'url du 1er site 1er site web de l'événement.
        """

        site_web = ''
        tmp_site_web = selector.xpath( 'td[3]/font/a/@href' ).extract_first(),

        if tmp_site_web[0] is not None :
            tmp_site_web = tmp_site_web[0]
            if 'javascript' not in tmp_site_web :
                site_web = tmp_site_web

        return site_web

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
