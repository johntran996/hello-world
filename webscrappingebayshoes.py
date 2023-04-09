from bs4 import BeautifulSoup
import requests
import re
import csv

csv_file = open('ebayScrape.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['url', 'listingName', 'price'])

#scrapes
url = 'https://www.ebay.com/itm/374616918598?epid=18059323676&hash=item5738e88a46:g:6t0AAOSw2MBkIa0P&amdata=enc%3AAQAHAAABAOTVLGSgN%2F%2FuDCGe%2FKDANoINVZMLr%2Bl%2Fli8styJ6aJ46zEcyV42zyNXSC34D1GbaS88UIuS%2FWbo8JQ2mSzKvVPWwIQ5hmD%2BYWcq9O904LEY2XEADSo1leViyu%2BvpNv8HVKCGyo8R2hmbGHtyqPmvBV5iRuFRCNs4jWP4PjLzCzlB2V2Pr0xexqN5hHZJqhvajvDsonzhx1F1uanZPe1N2g3k%2Bv5aiTJqSDNXadYf8cXpTtSU5veaCSeokWgN0YYxmXQb7XNxDJsCoPY4fdMdxn7xsjtxXlJ4Y0yCoOFLlXO89apR%2Fq%2BY8bOS24%2Fh8qGx9Gqv6uyoi%2FH4HYloUOPxAy8%3D%7Ctkp%3ABFBMzOSRt-xh'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
ebay = soup.find('body')

shoes = ebay.find('div', id = 'mainContent')
#for shoe name
shoeslisting = shoes.find('div',{'class': 'ux-bin-nudge__title'}).span.text


#for shoe price
shoesprice = shoes.find('div',{'class': 'vim-buybox-wrapper'})

shoepriceString = str(shoesprice)

shoespricepattern = r'US\s+\$?\d+\.?\d*'

match = re.search(shoespricepattern, shoepriceString)
print(url)
if match:
    shoePrice = match.group()
    print(shoePrice)

print(shoeslisting)

csv_writer.writerow([url, shoeslisting, shoePrice])

csv_file.close()
