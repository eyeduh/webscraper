import scrapy

class CategorySpider(scrapy.Spider):
    name = 'category'

    start_urls = ['http://www.sephora.com']

    def parse(self, response):
        for category in response.css('a.css-hzvn5z'):
            yield {'Category Name' : category.css('a::text').getall(), 
                   'Category Link' : category.css('a::attr(href)').getall(),
                              }
        

            