import scrapy
from scrapy_splash import SplashRequest

class TestMeJsSpider(scrapy.Spider):
    name = "test_me_js"
    #start_urls = ["https://www.leforem.be/particuliers/offres-emploi-recherche-par-arborescence.html"]
    # start_urls = ["https://www.leforem.be/particuliers/offres-emploi-recherche-par-arborescence.html"]
    start_urls = ["https://www.whatismybrowser.com/detect/is-javascript-enabled"]

    def start_requests(self):
        for url in self.start_urls:
            # yield scrapy.Request(url, self.parse ) # without javascript
            yield SplashRequest(url, self.parse ) # with javascript

    def parse(self, response):
        javascript_enabled = response.xpath( '//*[@id="main"]/section/div/div[1]/div/text()' ).extract_first()
        print( '###> Javascript is enabled ? : ' )
        print( '######> ' + javascript_enabled )

# refs:
# https://github.com/scrapy-plugins/scrapy-splash
# https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash/
