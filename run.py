from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lapscrap.spiders.best_picks import BestPicksSpider
from lapscrap.spiders.news import NewsSpider
from lapscrap.spiders.reviews import ReviewsSpider


process = CrawlerProcess(get_project_settings())

process.crawl(BestPicksSpider)
process.crawl(NewsSpider)
process.crawl(ReviewsSpider)

process.start()
