import scrapy

class ProductsSpider(scrapy.Spider):
    name = 'products'

    start_urls = ['http://www.sephora.com/brands-list']

    def parse(self, response):
        for brand in response.xpath('//a[@data-at="brand_link"]'):
            yield {
                'Brand' : brand.css('a::text').get(),
                'Brand URL' : 'http://www.sephora.com' + brand.xpath('//a/@href').get(),
                'Is It New' : brand.xpath('//span[@data-comp="Flag"]/text()').get(default='No'),
            }


            brand_urls = response.xpath('//a[@data-at="brand_link"]/@href')
            yield from response.follow_all(brand_urls, callback=self.parse_products)


    
    def parse_products(self, response):
        def extract_with_xpath(query):
            return response.xpath(query).get(default='').strip()
            
        yield {
            'Product Name' : extract_with_xpath('//span[@data-at="sku_item_name"]/text()'),
            'Product Brand' : extract_with_xpath('//span[@data-at="sku_item_brand"]/text()'),
            'Product URL' : extract_with_xpath('//a[@data-comp="ProductItem "]/@href'),
            'Product Image' : extract_with_xpath(('//img/@src')),
            'Product Price' : extract_with_xpath('//span[@data-at="sku_item_price_list"]/text()'),
            # 'Product Rating' : extract_with_xpath('//div[@data-comp="StarRating"]/@aria-label'),
                }
