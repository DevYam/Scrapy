import scrapy


class Test(scrapy.Spider):
    name = "Test"
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response, **kwargs):
        for item in response.css('.oxy-post-title'):
            yield {'Title': item.css('::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
