class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book: Book):
        if book:
            self.book_list.append(book)
    
    def find_by_author(self, author):
        return [book.title for book in self.book_list if author in book.author]
            
    
    def get_sorted_books_by_year(self):
        return sorted(self.book_list, key=lambda book: book.year)




if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Book A", "Author X", 2001))
    library.add_book(Book("Book B", "Author Y", 1999))
    library.add_book(Book("Book C", "Author X", 2010))

    print(library.find_by_author("Author X"))  # => ["Book A", "Book C"]
    print([book.title for book in library.get_sorted_books_by_year()])  # => ["Book B", "Book A", "Book C"]