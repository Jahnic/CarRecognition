from loguru import logger
import scrapy
from scrapy import Request
import scraper.spiders.spider_utils as utils
import scraper.items as items

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    locations = utils.get_start_urls()
    start_urls = locations[1:]  # auburn already finished 
    handle_httpstatus_list = [403]

    def parse(self, response):
        # Get urls
        link_objects = response.xpath('//a[@class="result-image gallery"]')
        for link in link_objects:
            url = link.xpath('@href').get()
            yield Request(url, callback=self.parse_page, meta={'URL': url})
        
        # Next page
        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)
        yield Request(absolute_next_url, callback=self.parse)

    
    def parse_page(self, response):
        item = items.ImageItem()
        url = response.meta.get('URL')
        car_brand = response.xpath('//p[@class="attrgroup"]/span/b/text()').extract_first()
        relative_image_urls = response.xpath('//a[@class="thumb"]/@href').getall()
        # list of image urls
        absolute_image_urls = []
        for img_url in relative_image_urls:
            absolute_image_urls.append(response.urljoin(img_url))
        
        # Fill remaining item fields
        item['listing_url'] = url
        item['car_brand'] = car_brand
        item['image_urls'] = absolute_image_urls
        yield item


    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)