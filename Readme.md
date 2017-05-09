# Evy

**Recherche et stock les événements**

# Role

* Récupérer des informations sur différents sites.
* Formater les informations afin de les stocké.

# Installation

Evy dépend de [scrapy](https://scrapy.org/) pour récupérer des données sur des sites tiers.

``pip install scrapy``

Certain site utilise javascript pour créer leurs contenus. Scrapy à besoin de [splash](https://github.com/scrapinghub/splash) pour capturer le javascript.

``pip install scrapy-splash``

Splash tourne sur un docker. Installation de docker sous debian.

``aptitude install docker-engine``


# Utilisation 

Lancer docker.

``docker run -p 8050:8050 scrapinghub/splash``

Exécuter un spider.

``cd ./spiderbox/ && scrapy crawl test_me_js``


# Liens

[Installation de splash et utilisation](https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash/)

[Scrapy-Splash](https://github.com/scrapy-plugins/scrapy-splash)

[Documentation Splash](http://splash.readthedocs.io/en/latest/api.html#)

