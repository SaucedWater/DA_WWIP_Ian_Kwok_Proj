import scrapy

class NewIan(scrapy.Spider):
    name = "new_IanKwok"
    start_urls = ["http://192.168.137.160/spicyx/"]
    def parse(self, response):
        for every_line in response.css("img"):
            yield {
                "The Image Link is": every_line.xpath('@src').extract_first(),
            }
            # To Recurse next page
            Page_selector = '.next ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )