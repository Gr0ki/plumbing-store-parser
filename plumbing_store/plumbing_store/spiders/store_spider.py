import scrapy


class StoreSpiderSpider(scrapy.Spider):
    name = 'store_spider'
    allowed_domains = ['https://best-dim.com/ua/g4861238-santehnika']
    start_urls = ['http://https://best-dim.com/ua/g4861238-santehnika/']

    def parse(self, response):
        pass
