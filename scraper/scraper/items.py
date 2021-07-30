# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageItem(scrapy.Item):
    # define the fields for your item here like:
    listing_url = scrapy.Field()
    car_brand = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    # IgnoreVisitedItems midlewares
    visit_id = scrapy.Field()
    visit_status = scrapy.Field()

    
