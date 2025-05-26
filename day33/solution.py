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


if __name__ == '__main__':
    book1 = Book("Python入門", "山田太郎", "978-4-0000-0000-1")
    book2 = Book("データ構造とアルゴリズム", "鈴木一郎", "978-4-0000-0000-2")
    Book.display_info(book1)
    Book.display_info(book2)
    Book.borrow(book1)
    Book.display_info(book1)
    Book.borrow(book1)
    Book.return_book(book1)
    Book.return_book(book1)
    Book.display_info(book1)
    Book.display_info(book2)