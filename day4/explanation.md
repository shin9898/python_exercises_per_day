# Day4 解説 - 図書館システム

## 模範回答

```python
from typing import List, Dict
from collections import defaultdict

class Book:
    def __init__(self, title: str, author: str, year: int, genre: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        if not book:
            raise ValueError("本が登録されていません")
        self.books.append(book)

    def search_by_author(self, author: str) -> List[str]:
        return [book.title for book in self.books if author in book.author]

    def filter_by_year(self, min_year: int) -> List[str]:
        return [book.title for book in self.books if book.year > min_year]

    def group_by_genre(self) -> Dict[str, List[str]]:
        grouped = defaultdict(list)
        for book in self.books:
            grouped[book.genre].append(book.title)
        return dict(grouped)

# テスト
if __name__ == '__main__':
    book1 = Book("Python入門", "田中", 2020, "技術書")
    book2 = Book("SQL徹底攻略", "佐藤", 2022, "技術書")
    book3 = Book("旅の記録", "田中", 2018, "旅行記")

    lib = Library()
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)

    print(lib.search_by_author("田中"))
    print(lib.filter_by_year(2019))
    print(lib.group_by_genre())
```

## 主なポイント

- `Library` は `Book` を「含む」関係（継承ではなく集約が正解）
- `search_by_author` と `filter_by_year` はリスト内包表記で実装
- `group_by_genre` では辞書を構築して分類する

## 型ヒントの重要性

各メソッドに型ヒントを付けることで関数の契約を明示できる：

```python
def search_by_author(self, author: str) -> List[str]:
```

## 改善点と発展

- クラスの継承関係を見直し、Library(Book) を Library に修正

- collections.defaultdict を使えば辞書の初期化を簡潔に書ける
