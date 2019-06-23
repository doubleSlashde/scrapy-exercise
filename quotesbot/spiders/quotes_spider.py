# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        quote_items = response.css("div.quote")
        for quote in quote_items:
            yield {
                # TODO: find the matching css classes for text and author
                'text': quote.css("").extract_first(),
                'author': quote.css("").extract_first(),
            }
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

