import scrapy

#links = //a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href

class SpiderCIA(scrapi.Spider):
    name = 'cia'
    start_urls = [
        'https://www.cia.gov/library/readingroom/historical-collections'
    ]
    custom_settings = {
        'FEED_URI': 'cia.json',
        'FEED_FORMAT': '.json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links_declassified = response.xpath('//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href')
        for link in links_declassified:
            yield response.follow(link, callback=self.parse_link)

        def parse_link(self, response):
            pass