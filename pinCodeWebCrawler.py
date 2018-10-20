'''
import beautifulscraper
# import libraries
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

print(1)
from bs4 import BeautifulSoup
print(2)
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
print(3)
page = urllib2.urlopen(quote_page)

print(2)
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('h1', attrs={'class': 'name'})

name = name_box.text.strip() # strip() is used to remove starting and trailing
print(name)
print(3)
# get the index price
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print(price)
'''
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
EOF
 scrapy runspider myspider.py



