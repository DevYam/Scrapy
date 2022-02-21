import scrapy


class HumorQuoteScrapper(scrapy.Spider):
    name = 'Humor Quote Scrapper'
    start_urls = ['http://quotes.toscrape.com/tag/humor/']


    def parse(self, response, **kwargs):
        for quote in response.css('.quote'):
            yield {'quote ': quote.css('span.text::text').get(),
                   'author': quote.xpath('span/small/text()').get()}


        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)




