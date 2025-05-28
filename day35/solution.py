import re

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def display_info(self):
        status = "利用可能" if self.is_available else "貸出中"
        print(f"タイトル: {self.title} 著者: {self.author} ISBN: {self.isbn} 状態: {status}")

    def borrow(self) -> bool:
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' が貸し出されました。")
            return True
        else:
            print(f"'{self.title}' は現在貸出中です。")
            return False

    def return_book(self) -> bool:
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' が返却されました。")
            return True
        else:
            print(f"'{self.title}' は既に利用可能です。")
            return False


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.books_by_isbn: dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("追加しようとしているオブジェクトはBookクラスのインスタンスではありません。")

        if book.isbn in self.books_by_isbn:
            print(f"警告: ISBN '{book.isbn}' の書籍 '{book.title}' は既に登録されています。")
            return

        self.books.append(book)
        self.books_by_isbn[book.isbn] = book
        print(f"'{book.title}' が図書館に追加されました。")

    def find_book(self, search_term: str) -> list[dict]:
        search_pattern = re.compile(re.escape(search_term), re.IGNORECASE)

        search_results = [
            {'title': book.title, 'isbn': book.isbn}
            for book in self.books
            if search_pattern.search(book.title) or search_pattern.search(book.isbn)
        ]

        print(f"検索結果: {search_results}")
        return search_results

    def _get_book_by_isbn(self, isbn: str) -> Book | None:
        """ISBNで書籍オブジェクトを効率的に検索する内部ヘルパーメソッド"""
        return self.books_by_isbn.get(isbn)

    def lend_book(self, isbn: str) -> bool:
        book_to_lend = self._get_book_by_isbn(isbn)
        if book_to_lend:
            return book_to_lend.borrow()
        else:
            print(f"ISBN: {isbn} の書籍は見つかりませんでした。")
            return False

    def receive_book(self, isbn: str) -> bool:
        book_to_receive = self._get_book_by_isbn(isbn)
        if book_to_receive:
            return book_to_receive.return_book()
        else:
            print(f"ISBN: {isbn} の書籍は見つかりませんでした。")
            return False

    def display_all_books(self) -> None:
        if not self.books:
            print("図書館に書籍は登録されていません。")
            return

        print("\n--- 全書籍リスト ---")
        for book in self.books:
            book.display_info()
        print("--------------------")


if __name__ == '__main__':
    book1 = Book("Python入門", "山田太郎", "978-4-0000-0000-1")
    book2 = Book("データ構造とアルゴリズム", "鈴木一郎", "978-4-0000-0000-2")
    book3 = Book("深層学習教科書", "橘一平", "978-4-0000-0000-3")
    book4 = Book("Python応用", "山田太郎", "978-4-0000-0000-1") # 同じISBNの書籍（テスト用）

    my_library = Library()

    print("\n--- 書籍の追加 ---")
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.add_book(book4) # 同じISBNの追加テスト

    print("\n--- 全書籍表示 ---")
    my_library.display_all_books()

    print("\n--- 書籍検索 ---")
    my_library.find_book("python入門") # 小文字でpythonの引数を渡す
    my_library.find_book("978")
    my_library.find_book("存在しない") # 検索結果なし

    print("\n--- 書籍の貸出 ---")
    my_library.lend_book("978-4-0000-0000-3") # 貸出成功
    my_library.display_all_books()
    my_library.lend_book("978-4-0000-0000-3") # 貸出中を再度借りる
    my_library.lend_book("978-4-0000-0000-4") # 存在しないisbn

    print("\n--- 書籍の返却 ---")
    my_library.receive_book("978-4-0000-0000-3") # 返却成功
    my_library.display_all_books()
    my_library.receive_book("978-4-0000-0000-4") # 存在しないisbn
    my_library.receive_book("978-4-0000-0000-3") # 利用可能を再度返却

    print("\n--- 最終書籍リスト ---")
    my_library.display_all_books()