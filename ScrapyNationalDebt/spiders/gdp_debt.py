import scrapy
import logging

class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ["https://www.worldpopulationreview.com/countries/countries-by-national-debt"]

    def parse(self, response):
        table = response.xpath('(//table)[1]/tbody/tr')
        for row in table:
            countryName = row.xpath('.//td[1]/a/text()').get()
            countryGdpRatio = row.xpath('.//td[2]/text()').get()
            countryPopulations = row.xpath('.//td[3]/text()').get()

            yield {
                "countryName": countryName,
                "countryGdpRatio": countryGdpRatio,
                "countryPopulations": countryPopulations
            }

