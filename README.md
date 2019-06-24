# Web scraping excercise with Scrapy

This is a Scrapy project to scrape quotes from famous people from http://quotes.toscrape.com.
This example was adopted from ([here](https://github.com/scrapinghub/spidyquotes)).
This project is only meant for educational purposes.

## Running the spiders

First, a working Python3 installation is required for running Scrapy.
Please use the Miniconda Python 3.7 installation for your OS, it can be found ([here](https://docs.conda.io/en/latest/miniconda.html))

For running Scrapy spiders, Scrapy has to be installed with the following command:
    
    $ conda install -c conda-forge scrapy 

Or if you already have a working Python installation with pip as package manager:

    $ pip install scrapy

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl quotes_spider

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl quotes_spider -o quotes.json
