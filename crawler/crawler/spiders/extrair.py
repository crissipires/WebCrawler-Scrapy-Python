import scrapy
from crawler.items import NewsItens

class ExtrairSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        urls = 'http://noosfero.ucsal.br/institucional/noticias/'
        yield scrapy.Request(url=urls, callback=self.parse)

    def parse(self, response):
        global notice
        for post in response.css("div.blog-post"):
            title = post.xpath('*//h1[@class="title"]/a/text()').get()
            date = post.xpath('*//span[@class="date"]/text()').get()
            link = post.xpath('*//h1[@class="title"]/a/@href').get()

            notice = NewsItens(title=title,date=date,link=link)
        yield notice

        next_page = response.xpath("*//a[@class='next_page']/@href").get()

        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page),callback=self.parse)



