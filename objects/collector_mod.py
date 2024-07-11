import requests
from bs4 import BeautifulSoup


class Collector:

    def __init__(self, url):
        self.url = url
        self.soup = self.get_webpage()
        self.data = None

    def get_webpage(self):
        headers = requests.utils.default_headers()
        headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })
        response = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def get_summary(self):
        self.show_notice()
        table_summary = self.soup.find(id='quote-summary')
        rows_summary = table_summary.find_all('tr')
        self.data = []
        for row in rows_summary:
            cells = row.find_all('td')
            row_data = []
            for cell in cells:
                row_data.append(cell.get_text())
            if row_data:
                self.data.append(row_data)
        return self.data

    def show_notice(self):
        notice = self.soup.find(id='quote-market-notice')
        print(notice.get_text())
