import scrapy


class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201004/1824032.htm']

    def parse(self, response):
        title = response.xpath('//h1').get()
        content = response.css('body#news>div:nth-of-type(4)>div:nth-of-type(2)>div:nth-of-type(9)>div>div>div:nth-of-type(2)>div>article>div>div:nth-of-type(4)').get()
        print(title)
        print(content)
