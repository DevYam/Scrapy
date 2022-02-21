import scrapy


class BlogSpider(scrapy.Spider):
    name = 'BlogSpider'
    start_urls = ['https://www.zyte.com/blog/']


    def parse(self, response, **kwargs):
        for title in response.css('.oxy-post-title'):
            yield {'title ': title.css('::text').get()}

        # Next button is an 'a' tag with class of next
        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)






# command to run "scrapy runspider ZyteBlogSpider.py -o blogtitle.jl"
# .jl is json lines format i.e new line delimited json
# we can also output to json or csv as we like



