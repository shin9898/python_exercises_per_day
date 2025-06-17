# フィードバック
from bs4 import BeautifulSoup

# ファイル読み込み部分はOK
with open('day42.html', encoding='utf-8') as fp:
    html_str = fp.read()

soup = BeautifulSoup(html_str, 'html5lib')

# 問1
# find() は要素が見つからない場合 None を返す可能性があるため、
# 安全のため None チェックを加えるか、Noneの場合はエラー処理を検討するとより堅牢です。
title = soup.find('title')
if title: # Noneチェックを追加
    print(title.text)
else:
    print("タイトルが見つかりませんでした。")


# 問2
# select() は常にリストを返すため、h1[0] のように直接インデックスにアクセスすると、
# リストが空の場合 (要素が見つからない場合) に IndexError が発生する可能性があります。
# 安全のため、リストが空でないかを確認する処理を加えるのがベストです。
h1_elements = soup.select('#header > h1')
if h1_elements: # リストが空でないかを確認
    print(h1_elements[0].string)
else:
    print("h1要素が見つかりませんでした。")


# 問3
# 素晴らしいです！ select() で取得したリストをループして処理できています。
description_list = soup.select('p.description')
for description in description_list:
    # .string は子要素がテキストのみの場合に推奨されますが、
    # .text や .get_text() は子要素にタグが含まれる場合でも、その中のテキストを全て取得できるため、
    # より汎用的に使われます。今回のケースではどちらでも問題ありません。
    print(description.string)


# 問4
# 完璧です！
product_item_list = soup.select('div.product-item')
print(len(product_item_list))


# 問5
# select() で取得したリストに対するインデックスアクセスは、問2と同様に IndexError のリスクがあります。
# ここもリストの存在チェックを加えるとより安全です。
item_101_h2_elements = soup.select('#item-101 > h2')
if item_101_h2_elements: # リストが空でないかを確認
    print(item_101_h2_elements[0].string)
else:
    print("商品名が見つかりませんでした。")

item_101_amount_elements = soup.select('#item-101 > p.price > .amount')
if item_101_amount_elements: # リストが空でないかを確認
    print(item_101_amount_elements[0].string)
else:
    print("価格が見つかりませんでした。")


# 問6
# find_all と get() の組み合わせも適切です。
# リスト内包表記を使うと、よりPythonicに書くことも可能です。
detail_link_all = soup.find_all('a', class_='detail-link')
href_values = []
for link in detail_link_all:
    href_values.append(link.get('href'))
print(href_values)

# 参考：リスト内包表記での書き方
# href_values_comprehension = [link.get('href') for link in soup.find_all('a', class_='detail-link')]
# print(href_values_comprehension)