from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["sachvui.vn"]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    start_urls = [
        "https://sachvui.vn/",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//a[@class="vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-rounded vc_btn3-style-3d vc_btn3-block vc_btn3-color-primary"]/a')

        for question in questions:
            item = CrawlerItem()

            print(question);
            item['Title'] = question.xpath('title').extract()
            item['URL'] = question.xpath('href').extract()
            # item['Time'] = question.xpath(
            #     'div[@class="actionuser"]/a[@class="time"]/text()').extract_first()

            yield item
