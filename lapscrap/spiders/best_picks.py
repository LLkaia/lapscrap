import scrapy

from ..items import ArticleItem


class BestPicksSpider(scrapy.Spider):
    name = "best_picks"
    allowed_domains = ['laptopmag.com']
    start_urls = [f'https://www.laptopmag.com/search/page/{i}?articleType=best-pick' \
                  f'&searchTerm=laptops&sortBy=publishedDate' for i in range(1, 10)]

    def parse(self, response):
        laptops = response.css('div.listingResult')
        for laptop in laptops:
            item = ArticleItem()
            item['link'] = laptop.css('a.article-link::attr(href)').get()
            item['image'] = laptop.css('img::attr(data-pin-media)').get()
            item['title'] = laptop.css('h3.article-name::text').get().strip()
            item['author'] = laptop.css('span[style="white-space:nowrap"]::text').get().strip()
            item['date'] = laptop.css('time::attr(datetime)').get()
            item['description'] = laptop.css('p.synopsis::text').get().strip()
            item['tags'] = item['title'].split()
            item['content'] = []
            yield item
