import json

from scrapy.exceptions import DropItem


class ArticlePipeline:
    def open_spider(self, spider):
        self.file = open("laptops.json", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if not item.get("title"):
            raise DropItem(f"Missing title in {item}")
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


