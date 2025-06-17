```python
from bs4 import BeautifulSoup
# html5libを使うには、事前に `pip install html5lib` が必要です。
```
```python
# --- 【HTMLの抜粋】 ---
html_doc = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>商品情報ページ</title>
</head>
<body>
    <div id="header">
        <h1>商品リスト</h1>
        <p class="description">最新の商品情報を提供しています。</p>
    </div>

    <div class="product-list">
        <div class="product-item" id="item-101">
            <h2>Python入門</h2>
            <p class="price">価格: <span class="amount">2500</span>円</p>
            <a href="/products/101" class="detail-link">詳細を見る</a>
        </div>

        <div class="product-item" id="item-102">
            <h2>JavaScript実践</h2>
            <p class="price">価格: <span class="amount">3000</span>円</p>
            <a href="/products/102" class="detail-link">詳細を見る</a>
        </div>

        <div class="product-item" id="item-103">
            <h2>Web開発基礎</h2>
            <p class="price">価格: <span class="amount">2800</span>円</p>
            <a href="/products/103" class="detail-link">詳細を見る</a>
        </div>
    </div>

    <div id="footer">
        <p>&copy; 2025 Sample Inc.</p>
        <a href="/contact" class="contact-link">お問い合わせ</a>
    </div>
</body>
</html>
"""

# --- 【前提コード】 ---
# ここがポイント！ html5libパーサーを使用しています。
soup = BeautifulSoup(html_doc, 'html5lib')
```

# --- 【問題】 ---

# 問1.
# ページのタイトルタグ <title> のテキストを取得し、出力するコードを記述しなさい。

# 問2.
# idが `header` の `div` タグの中にある `h1` タグのテキストを取得し、出力するコードを記述しなさい。

# 問3.
# クラス名が `description` の `p` タグのテキストを取得し、出力するコードを記述しなさい。

# 問4.
# すべての商品アイテム（クラス名が `product-item` の `div` タグ）をリストとして取得し、そのリストの要素数を表示するコードを記述しなさい。

# 問5.
# 最初の `product-item` （idが `item-101` の `div` タグ）の中から、商品名（`<h2>` タグのテキスト）と価格（クラス名が `amount` の `<span>` タグのテキスト）を取得し、それぞれ出力するコードを記述しなさい。

# 問6.
# すべての「詳細を見る」リンク（クラス名が `detail-link` の `a` タグ）の `href` 属性の値をリストとして取得し、出力するコードを記述しなさい。


# --- 【解答例】 (問題を解いた後に、この下のコメントアウトを外して確認してください) ---
"""
print("--- 問1 ---")
title_tag = soup.find('title')
if title_tag:
    print(title_tag.get_text())

print("\n--- 問2 ---")
header_div = soup.find(id='header')
if header_div:
    h1_tag = header_div.find('h1')
    if h1_tag:
        print(h1_tag.get_text())

print("\n--- 問3 ---")
description_p = soup.find('p', class_='description')
if description_p:
    print(description_p.get_text())

print("\n--- 問4 ---")
product_items = soup.find_all('div', class_='product-item')
print(f"商品アイテムの数: {len(product_items)}")

print("\n--- 問5 ---")
first_item = soup.find(id='item-101')
if first_item:
    product_name_h2 = first_item.find('h2')
    price_span = first_item.find('span', class_='amount')
    if product_name_h2 and price_span:
        print(f"商品名: {product_name_h2.get_text()}")
        print(f"価格: {price_span.get_text()}円")

print("\n--- 問6 ---")
detail_links = soup.find_all('a', class_='detail-link')
href_values = []
for link in detail_links:
    href_values.append(link.get('href'))
print(href_values)
"""