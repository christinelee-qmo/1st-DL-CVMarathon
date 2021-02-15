import scrapy
from Day025.items import ScrapyDemoItem


class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201004/1824032.htm']

    def parse(self, response):
        item = ScrapyDemoItem()
        item['title'] = response.xpath('//title/text()').get()
        item['content'] = response.xpath('//div[@itemprop="articleBody"]//p/text()').getall()
        yield item