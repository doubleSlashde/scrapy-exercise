import scrapy
from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'quotes_spider'])
# or use CLI -> scrapy crawl quotes_spider -o file.csv -t csv