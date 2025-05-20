📘【Python 1日1問 - Day26】

🧩 **問題：売上集計と最大カテゴリの出力**

ある店舗の1日の売上記録が、以下のような形式のリストで与えられます：

```python
sales = [
    {"name": "りんご", "price": 120, "category": "食品"},
    {"name": "Tシャツ", "price": 1500, "category": "衣類"},
    {"name": "パン", "price": 200, "category": "食品"},
    {"name": "ズボン", "price": 3000, "category": "衣類"},
    {"name": "ボールペン", "price": 100, "category": "文房具"},
    {"name": "ノート", "price": 150, "category": "文房具"},
    {"name": "シャーペン", "price": 120, "category": "文房具"}
]
```

このリストをもとに、以下の処理を行う関数 max_sales_category(sales: list[dict]) -> str を作成してください。

🎯 要件

1. 各カテゴリ（"食品"・"衣類"・"文房具"）ごとの売上合計金額を算出する。

2. 最も売上金額が高かったカテゴリ名を文字列で返す。

3. 複数同じ最大金額カテゴリがある場合は、出現順で最初のカテゴリ名を返す。

4. priceがintでない場合は ValueError を出す。

💡 ヒント

- collections.defaultdict や max() 関数が役立つかもしれません。

- 集計後の辞書から、最大値を持つキーを抽出する方法を考えてみましょう。

- テストコードも必ず if __name__ == "__main__": 以下に記述してください。

🧪 出力例

```python
print(max_sales_category(sales))  # "衣類"
```