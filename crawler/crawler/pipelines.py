# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import os

from scrapy.exceptions import DropItem
import signal


class CrawlerPipeline:
    def open_spider(self,spider):
        self.file = open('notices.json', 'w')

    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        ANO = '2021'
        if ANO in item['date']:
            line = json.dumps(dict(item)) + '\n'
            self.file.write(line)
            return item
        else:
            os.kill(os.getpid(), signal.SIGINT)
            os.kill(os.getpid(), signal.SIGINT)


