## 🧠 解説

### ✅ 実装内容チェック

- ✅ `Book` クラスの定義：`title`, `author`, `year` 属性が正しく実装されている
- ✅ `Library` クラス：書籍の追加・検索・ソートの各メソッドが機能している
- ✅ `find_by_author()`：部分一致検索として `author in book.author` の条件が使われている
- ✅ `get_sorted_books_by_year()`：`lambda` 関数で出版年でのソートが行われている

全体的に正確かつシンプルに実装されています！👏

---

### 💡 改善ポイント

#### 1. `find_by_author` の引数の型ヒントがない

以下のように明示することで、読みやすさと補完機能の向上につながります：

```python
def find_by_author(self, author: str) -> list[str]:
```

#### 2. `hasattr(book)` チェックはなくても OK

現状の `add_book()` 内の `if book:` チェックは冗長です。
クラスの利用前提であり、None チェックを行うケースはあまり想定されないため、省略しても問題ありません。

---

### ✨ 模範解答（参考）

```python
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.book_list: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.book_list.append(book)

    def find_by_author(self, author: str) -> list[str]:
        return [book.title for book in self.book_list if author in book.author]

    def get_sorted_books_by_year(self) -> list[Book]:
        return sorted(self.book_list, key=lambda book: book.year)

if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Book A", "Author X", 2001))
    library.add_book(Book("Book B", "Author Y", 1999))
    library.add_book(Book("Book C", "Author X", 2010))

    print(library.find_by_author("Author X"))  # => ["Book A", "Book C"]
    print([book.title for book in library.get_sorted_books_by_year()])  # => ["Book B", "Book A", "Book C"]
```

---

### 総評

クラスの構造もメソッドの粒度も非常に良く、Python らしい簡潔な実装ができています。
次回以降では「複数条件でのソート」や「検索条件のカスタマイズ」など、もう一歩進んだ設計にも挑戦していきましょう 💪

Day9、お疲れさまでした！🎉
