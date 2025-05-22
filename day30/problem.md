📝 Python基礎力強化 - Day30
目的
filter()関数とラムダ式を用いて、特定の条件を満たす要素を効率的に抽出する。
複数の条件を組み合わせたフィルタリングと、抽出後のデータ加工を行う。
any()やall()のような、条件判定に役立つ組み込み関数を理解する（直接使う必要はないかもしれませんが、考え方として）。
問題
あなたはIT機器販売会社のデータアナリストです。
以下の製品データ（リスト内に辞書形式で格納されています）が与えられます。

```Python

products = [
    {"product_id": "P001", "name": "Laptop Pro", "category": "Laptop", "price": 150000, "stock": 5, "tags": ["high-performance", "business"]},
    {"product_id": "P002", "name": "Basic Mouse", "category": "Peripheral", "price": 2500, "stock": 50, "tags": ["office", "wireless"]},
    {"product_id": "P003", "name": "Gaming Keyboard", "category": "Peripheral", "price": 12000, "stock": 10, "tags": ["gaming", "mechanical"]},
    {"product_id": "P004", "name": "Ultrabook Air", "category": "Laptop", "price": 180000, "stock": 3, "tags": ["thin", "portable", "business"]},
    {"product_id": "P005", "name": "External SSD 1TB", "category": "Storage", "price": 18000, "stock": 15, "tags": ["fast", "portable"]},
    {"product_id": "P006", "name": "Wireless Headset", "category": "Audio", "price": 7000, "stock": 20, "tags": ["wireless", "gaming"]},
    {"product_id": "P007", "name": "4K Monitor 27inch", "category": "Monitor", "price": 45000, "stock": 7, "tags": ["high-resolution", "display"]},
    {"product_id": "P008", "name": "Webcam HD", "category": "Peripheral", "price": 4000, "stock": 30, "tags": ["video", "office"]},
]
```
以下の要件を満たすPythonコードを記述してください。

以下の両方の条件を満たす製品のみを抽出する。
stock (在庫数) が 10以下 である。
tags (タグ) に "business" または "gaming" のいずれかのタグが含まれている。
抽出された製品を、price (価格) が安い順にソートする。もし価格が同じ場合は、product_id (製品ID) の昇順でソートする。
最終的にソートされた製品リストから、各製品の "name" と "price" のみを抽出し、新しい辞書のリストとして出力する。
期待する出力例:

```Python

[
    {'name': 'Gaming Keyboard', 'price': 12000},
    {'name': 'External SSD 1TB', 'price': 18000}, # 'business' or 'gaming' tag is NOT required for this example, but just for illustrative purpose of price sort. It would be filtered out by tag condition.
    {'name': '4K Monitor 27inch', 'price': 45000},
    {'name': 'Laptop Pro', 'price': 150000},
    {'name': 'Ultrabook Air', 'price': 180000}
]
```
※注意点：期待する出力例は、問題の条件を全て満たした場合の正確な出力とは異なる可能性があります。ご自身で正確な出力を作成してください。あくまで出力形式の参考です。

filter()をどのように使うか、条件の組み合わせ方をどう表現するか、そしてDay29で学んだソートの知識をどう活かすかがポイントです。
