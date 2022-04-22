from requests import Response
import scrapy


class HakosSpider(scrapy.Spider):
    name = "hakos"
    start_urls = [
        "https://ln.hako.re/xuat-ban",
    ]

    def parse(self, response, **kwargs):
        listall_details = response.xpath("//div[@class='listall-detail']")
        for listall_detail in listall_details:
            yield self.extract_data_from_selector(listall_detail)

        paging_urls = response.xpath("//a[contains(@class, 'page_num')]/@href").getall()
        yield from response.follow_all(paging_urls, self.parse)

    def extract_data_from_selector(self, selector : scrapy.Selector) -> dict:
        data = dict()
        book = selector.xpath(".//a[@class='series-name']/text()").get()
        if len(book) > 1:
            data["name"] = book
            data["series"] = book.split("-")[0].strip()
        else:
            data["name"] = data["series"] = book[0].strip()

        data["publisher"] = selector.xpath(".//span[@class='publisher-name']/a/text()").get()
        info_items = selector.xpath(".//div[contains(@class,'info-item')]")
        for index, info_item in enumerate(info_items):
            if index == 0:
                data["author"] =  info_item.xpath(".//span[@class='info-value']/a/text()").get()
            if index == 1:
                data["artist"] =  info_item.xpath(".//span[@class='info-value']/a/text()").get()
            if index == 2:
                data["translator"] =  info_item.xpath(".//span[@class='info-value']/a/text()").get()
            if index == 4:
                data["date_published"] =  info_item.xpath(".//span[@class='info-value']/text()").get()
            if index == 5:
                data["price"] =  info_item.xpath(".//span[@class='info-value']/text()").get()
                
        return data
