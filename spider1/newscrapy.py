#############################
#Title: Python Project
#Name: Ian Kwok
#Class: PN2104L

#########################
#Import scrapy
###########################
import scrapy

#####################
#Class Branch- Web Scraping
##################
class NewIan(scrapy.Spider):
    name = "new_IanKwok"
    #Set target URL
    start_urls = ["http://192.168.137.160/spicyx/"]
    def parse(self, response):
        for every_line in response.css("img"):
            yield {
                "The Image Link is": every_line.xpath('@src').extract_first(),
            }
            # To Recurse next page
            Page_selector = '.next ::attr(href)'
            #extract content of website
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )