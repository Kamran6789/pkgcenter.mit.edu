from datetime import datetime
import pyairtable
import scrapy
from scrapy.crawler import CrawlerProcess


class PkgcenterSpider(scrapy.Spider):
    name = "pkgcenter"
    start_urls = ["https://pkgcenter.mit.edu/programs/ideas/"]

    def parse(self, response):
        items = {}
        items["competition"] = 'IDEAS'
        items['year'] = '2023'
        items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        items['winner business'] = response.css("p+ ul ::text").extract()[2]
        items['2nd place business'] = response.css("p+ ul ::text").extract()[5]
        items['3rd place business'] = response.css("p+ ul ::text").extract()[9].replace('\xa0', '').replace('(', '').replace(')', '')
        items['4th place business'] = response.css("p+ ul ::text").extract()[12]

        table.create(items)


if __name__ == '__main__':
    api = pyairtable.Api('patAutBB8czI3ifML.c1e5aa28bb6f09cbb0d81815494d371003902e6f43500abebe713f307a505f25')
    base = api.base('appISH2KhnZt5ElD8')
    table = [v for v in base.tables() if v.name == 'Main Table'][0]
    process = CrawlerProcess()
    process.crawl(PkgcenterSpider)
    process.start()
