class Book:
    def __init__(self, title: str, author: str, year: int, genre: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self,book):
        if not book:
            raise ValueError("本が登録されていません")
        else:
            self.books.append(book)

    def search_by_author(self, author):
        result = [book.title for book in self.books if author in book.author]
        return result

    def filter_by_year(self, min_year):
        result = [book.title for book in self.books if min_year < book.year]
        return result
    
    def group_by_genre(self):
        group_by_genre_dict = {}
        for book in self.books:
            if book.genre not in group_by_genre_dict:
                group_by_genre_dict[book.genre] = [book.title]
            else:
                group_by_genre_dict[book.genre].append(book.title)
        return group_by_genre_dict


if __name__ == '__main__':
    book1 = Book("Python入門", "田中", 2020, "技術書")
    book2 = Book("SQL徹底攻略", "佐藤", 2022, "技術書")
    book3 = Book("旅の記録", "田中", 2018, "旅行記")

    lib = Library()
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)

    print(lib.search_by_author("田中"))  
    # => ["Python入門", "旅の記録"]

    print(lib.filter_by_year(2019))     
    # => ["Python入門", "SQL徹底攻略"]

    print(lib.group_by_genre())         
    # => {"技術書": ["Python入門", "SQL徹底攻略"], "旅行記": ["旅の記録"]}


# 模範回答
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
