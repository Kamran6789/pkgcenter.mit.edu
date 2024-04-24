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

        yield(items)


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(PkgcenterSpider)
    process.start()
