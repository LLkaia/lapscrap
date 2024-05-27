import scrapy


class ArticleItem(scrapy.Item):
    link = scrapy.Field()
    image = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    description = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
