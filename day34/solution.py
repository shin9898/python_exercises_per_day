import re

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def display_info(self):
        if self.is_available is True:
            is_available = "利用可能"
        else:
            is_available = "貸出中"
        print(f"タイトル: {self.title} 著者: {self.author} ISBN: {self.isbn} 状態: {is_available}")

    def borrow(self):
        if self.is_available is True:
            self.is_available = False
            print(f"{self.title}が貸し出されました")
        else:
            print(f"{self.title}は現在貸出中です")

    def return_book(self):
        if self.is_available is False:
            self.is_available = True
            print(f"{self.title}が返却されました")
        else:
            print(f"{self.title}は既に利用可能です")


class Library:
    def __init__(self):
        self.books = []


    def add_book(self, book: Book) -> None:
        if not book:
            raise ValueError("不正な値が含まれています。")
        self.books.append(book)
        print(f"{book.title}が図書館に追加されました。")

    def find_book(self, search_term: str) -> list[dict]:
        search_results = []
        search_pattern = re.compile(re.escape(search_term), re.IGNORECASE)

        for book in self.books:
            title_match = search_pattern.search(book.title)
            isbn_match = search_pattern.search(book.isbn)
            if title_match or isbn_match:
                search_results.append({'title': book.title, 'isbn': book.isbn})
        print(search_results)
        return search_results


    def lend_book(self, isbn: str):
        result_book = []
        for book in self.books:
            if isbn not in book.isbn:
                continue
            else:
                book.borrow()
                result_book.append(book)
                break
        if len(result_book) == 0:
            print(f"ISBN: {isbn}の書籍は見つかりませんでした。")

    def receive_book(self, isbn):
        result_book = []
        for book in self.books:
            if isbn not in book.isbn:
                continue
            else:
                book.return_book()
                result_book.append(book)
                break
        if len(result_book) == 0:
            print(f"ISBN: {isbn}の書籍は見つかりませんでした。")

    def display_all_books(self) -> None:
        if not self.books:
            print("図書館に書籍は登録されていません。")
        for book in self.books:
            book.display_info()




if __name__ == '__main__':
    book1 = Book("Python入門", "山田太郎", "978-4-0000-0000-1")
    book2 = Book("データ構造とアルゴリズム", "鈴木一郎", "978-4-0000-0000-2")
    book3 = Book("深層学習教科書", "橘一平", "978-4-0000-0000-3")
    my_library = Library()
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.display_all_books()
    my_library.find_book("python入門") # 小文字でpythonの引数を渡す
    my_library.find_book("978")
    my_library.lend_book("978-4-0000-0000-3")
    my_library.lend_book("978-4-0000-0000-4") # 存在しないisbn
    my_library.receive_book("978-4-0000-0000-3")
    my_library.receive_book("978-4-0000-0000-4") # 存在しないisbn
    my_library.receive_book("978-4-0000-0000-3") # 利用可能なisbn
    my_library.display_all_books()