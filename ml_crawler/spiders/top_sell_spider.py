import scrapy
import re

class TopSellSpider(scrapy.Spider):
    name = "top_sell"

    def start_requests(self):
        urls = [
            'https://lista.mercadolivre.com.br/arduino#D[A:arduino]'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for item in response.css('li.results-item'):
            
            n_sells = 0
            item_condition = item.css('div.item__condition::text').extract_first()
            state = 'N/A'

            try:
                n_sells = int(re.search(r'\d+', item_condition).group())
                state = item_condition.split('-')[1]
            except Exception as e:
                print e

            yield {
                'name': item.css('span.main-title::text').extract_first(),
                'n_sells': n_sells,
                'state': state
            }

        next_page = response.css('li.pagination__next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)