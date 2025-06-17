from bs4 import BeautifulSoup

with open('day42.html', encoding='utf-8') as fp:
    html_str = fp.read()

soup = BeautifulSoup(html_str, 'html5lib')

# 問1
title = soup.find('title')
print(title.text)

# 問2
h1 = soup.select('#header > h1')
print(h1[0].string)

# 問3
description_list = soup.select('p.description')
for description in description_list:
    print(description.string)

# 問4
product_item_list = soup.select('div.product-item')
print(len(product_item_list))

# 問5
item_101_h2 = soup.select('#item-101 > h2')
print(item_101_h2[0].string)
item_101_amount = soup.select('#item-101 > p.price > .amount')
print(item_101_amount[0].string)

# 問6
detail_link_all = soup.find_all('a', class_='detail-link')
href_values = []
for link in detail_link_all:
    href_values.append(link.get('href'))
print(href_values)