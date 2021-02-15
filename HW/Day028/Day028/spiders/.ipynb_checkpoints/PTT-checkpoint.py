import scrapy
from Day028.items import ScrapyDemoItem

class PttSpider(scrapy.Spider):
    name = 'PTT'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Baseball/M.1613320031.A.2F3.html','https://www.ptt.cc/bbs/Baseball/M.1613321185.A.F7F.html']

    def parse(self, response):
        item = ScrapyDemoItem()
        item['url'] = response.url
        item['title'] = response.xpath('(//span[@class="article-meta-value"])[3]/text()').get()
        item['content'] = response.xpath('//div[@id="main-container"]//div/text()').getall()
        yield item

