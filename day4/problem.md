# Day4 - 図書館システム（本の検索・分類）

以下の 2 つのクラスを作成し、本の管理を行う簡単な図書館システムを実装してください。

## Book クラス

- `title`（タイトル）, `author`（著者）, `year`（出版年）, `genre`（ジャンル）

## Library クラス

- メソッド
  - `add_book(book: Book)`：本を追加
  - `search_by_author(author: str)`：著者名で検索
  - `filter_by_year(min_year: int)`：指定年より新しい本を取得
  - `group_by_genre()`：ジャンルごとに本を分類

## 実行例

```python
book1 = Book("Python入門", "田中", 2020, "技術書")
book2 = Book("SQL徹底攻略", "佐藤", 2022, "技術書")
book3 = Book("旅の記録", "田中", 2018, "旅行記")

lib = Library()
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

print(lib.search_by_author("田中"))
# ["Python入門", "旅の記録"]

print(lib.filter_by_year(2019))
# ["Python入門", "SQL徹底攻略"]

print(lib.group_by_genre())
# {"技術書": ["Python入門", "SQL徹底攻略"], "旅行記": ["旅の記録"]}
```
