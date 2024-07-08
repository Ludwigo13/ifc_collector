import scrapy


class MySpider(scrapy.Spider):
    name = 'my_spider'

    def __init__(self, url=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        quote_summary = response.xpath('//*[@id="quote-summary"]')
        if not quote_summary:
            self.logger.warning('No div found with ID quote-summary')
            return

        divs = quote_summary.xpath('.//div[contains(@data-test, "summary-table")]')
        if not divs:
            self.logger.warning('No divs found with class containing "summary-table"')

        for div in divs:
            table = div.xpath('.//table')
            if not table:
                self.logger.warning('No table found within div')
                continue

            rows = table.xpath('.//tr')
            for row in rows:
                name = row.xpath('.//td[contains(@class, "C")]//span/text()').get()
                value = row.xpath('.//td[contains(@class, "Ta")]//text()').get()

                if name and value:
                    yield {
                        'name': name.strip(),
                        'value': value.strip(),
                    }
                else:
                    self.logger.warning('Missing name or value in row: %s', row.get())
