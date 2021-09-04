# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import os

import signal


class CrawlerPipeline:

    def __init__(self):
        self.file = open('news.json', 'w')

    def open_spider(self, spider):
        self.file.write("[")

    def close_spider(self, spider):
        self.file.write("]")
        self.file.close()

    def process_item(self, item, spider):
        YEAR = '2021'
        if YEAR in item['date']:
            line = json.dumps(
                dict(item),
                sort_keys=True,
                indent=4,
                ensure_ascii=False,
                separators=(',', ': ')
            ) + ",\n"

            self.file.write(line)

            return item
        else:
            #force to stop
            os.kill(os.getpid(), signal.SIGINT)
            os.kill(os.getpid(), signal.SIGINT)
