import requests
from bs4 import BeautifulSoup


class Collector:

    def __init__(self, url):
        self.url = url
        self.soup = self.get_webpage()
        self.data = None

    def get_webpage(self):
        response = requests.get(self.url).content
        soup = BeautifulSoup(response, 'html.parser')
        return soup

    def get_summary(self):
        table_prevision = self.soup.find(id='quote-summary')
        rows_prevision = table_prevision.find_all('tr')
        self.data = []
        for row in rows_prevision:
            cells = row.find_all('td')
            row_data = []
            for cell in cells:
                row_data.append(cell.get_text())
            if row_data:
                self.data.append(row_data)
        return self.data