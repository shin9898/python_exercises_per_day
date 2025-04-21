# Day9 問題文

## 📘 内容

あなたは書籍管理システムを開発しています。以下の要件を満たす `Book` クラスと `Library` クラスを設計・実装してください。

- 各 `Book` はタイトル（`title`）、著者（`author`）、出版年（`year`）を属性に持つ
- `Library` クラスは複数の書籍を管理し、以下の操作を提供する：
  - 書籍の追加（`add_book(book: Book)`）
  - 著者名で書籍を検索（`find_by_author(author: str)`）
  - 出版年順に書籍を昇順で取得（`get_sorted_books_by_year()`）

## 🧩 条件

- 出力やファイル操作は不要です
- ソートには `sorted()` を使用して構いません

## 🔍 目的

- クラスの設計力
- リストのフィルタリング・ソート処理の実装力
- 型ヒント・メソッド定義の構造化力

---

## 🧪 テストコード例（任意）

以下のようなテストコードで動作確認ができると望ましい：

```python
if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Book A", "Author X", 2001))
    library.add_book(Book("Book B", "Author Y", 1999))
    library.add_book(Book("Book C", "Author X", 2010))

    print(library.find_by_author("Author X"))  # => ["Book A", "Book C"]
    print([book.title for book in library.get_sorted_books_by_year()])  # => ["Book B", "Book A", "Book C"]
```
