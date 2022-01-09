import scrapy
import csv

class QuotesSpider(scrapy.Spider):
    name = "project"

    def start_requests(self):
        urls = [
            "https://www.tgju.org/"
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        for i in range(len(response.css(".info-bar h3::text").getall())):
            yield {
                "value":response.css(".info-bar h3::text").getall()[i],
                "price":response.css(".info-price::text").getall()[i]
            }
        

        

            
            
            
        

        
         
