📝 Python基礎力強化 - Day29
目的
sorted() 関数とラムダ式、条件分岐を組み合わせて複雑なデータの並べ替えと抽出を行う。
複数の条件に基づくフィルタリングとソートのロジックを理解する。
問題
あなたはオンラインショップの管理者で、注文履歴データを分析しています。
以下の注文データ（リスト内に辞書形式で格納されています）が与えられます。

```Python

orders = [
    {"order_id": "A001", "item": "Laptop", "price": 120000, "quantity": 1, "status": "shipped"},
    {"order_id": "A002", "item": "Mouse", "price": 3000, "quantity": 2, "status": "pending"},
    {"order_id": "A003", "item": "Keyboard", "price": 8000, "quantity": 1, "status": "shipped"},
    {"order_id": "A004", "item": "Monitor", "price": 25000, "quantity": 1, "status": "pending"},
    {"order_id": "A005", "item": "Laptop", "price": 150000, "quantity": 1, "status": "shipped"},
    {"order_id": "A006", "item": "Webcam", "price": 5000, "quantity": 3, "status": "shipped"},
    {"order_id": "A007", "item": "SSD", "price": 10000, "quantity": 2, "status": "cancelled"},
    {"order_id": "A008", "item": "Mouse", "price": 3500, "quantity": 1, "status": "shipped"},
]
```
以下の要件を満たすPythonコードを記述してください。

ステータスが "shipped" である注文のみを抽出する。
抽出された注文を、price (価格) が高い順にソートする。もし価格が同じ場合は、order_id (注文ID) の昇順でソートする。
最終的にソートされた注文リストから、各注文の "order_id" と "item"、"price" のみを抽出し、新しい辞書のリストとして出力する。
期待する出力形式:

```Python

[
    {'order_id': 'A005', 'item': 'Laptop', 'price': 150000},
    {'order_id': 'A001', 'item': 'Laptop', 'price': 120000},
    {'order_id': 'A003', 'item': 'Keyboard', 'price': 8000},
    {'order_id': 'A006', 'item': 'Webcam', 'price': 5000},
    {'order_id': 'A008', 'item': 'Mouse', 'price': 3500}
]
```