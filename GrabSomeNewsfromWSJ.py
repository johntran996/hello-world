from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.wsj.com/'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
soup = soup.find_all('script')

soup = str(soup[20])

headlines = re.findall(r'"headline":"([^"]+)"', soup)

headlines = list(set(headlines))

for i, x in enumerate(headlines):
    print(f'{x}')
