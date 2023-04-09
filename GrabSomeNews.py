from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.wsj.com/'
url1 = 'https://www.nytimes.com'

url = 'https://www.wsj.com/'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
soup = soup.find('div', id = 'root')
soup = soup.find_all('a', class_="")
soup = str(soup)

source1 = requests.get(url1).text
soup1 = BeautifulSoup(source1, 'lxml')
soup1 = soup1.find('main', id = 'site-content')
soup1 = (soup1)
soup1 = str(soup1)



headlines = re.findall(r'title="([^"]+)"', soup)
headlines1 = re.findall(r'<h3\s+class="indicate-hover css-66vf3i">(.*?)</h3>', soup1)

#Wall Street Journal

print('WallStreet Journal')
for i, x in enumerate(headlines):
    print(f'{x}')



print('\n\n\n\nNY Times')
for i, x in enumerate(headlines1):
    print(f'{x}')

