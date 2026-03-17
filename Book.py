class Book:
    def __init__(self,book_id,book_title, book_category, book_author,book_selling_price, book_import_price, book_publisher) :
        self.book_id=book_id
        self.book_title=book_title
        self.category =book_category 
        self.author=book_author 
        self.status= "unavailable"
        self.selling_price=book_selling_price 
        self.import_price=book_import_price 
        self.book_publisher= book_publisher
        self.available_copies = 0
    def update_status(self):
        if self.available_copies > 0:
            self.status = "available"
        else:
            self.status = "unavailable"
    def __str__(self):
        return (f"ID: {self.book_id}, Title: {self.book_title}, Author: {self.author}, "
                f"Category: {self.category}, Status: {self.status}, "
                f"Sell: {self.selling_price} VND, Import: {self.import_price} VND")

class BookManager: 
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        book.update_status()
        self.books.append(book)
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return
        print("Book not found!")
    def update_book(self,book_id,new_price=None,copies=None):
        for book in self.books:
            if book.book_id == book_id:
                if new_price is not None:
                    book.selling_price = new_price
                if copies is not None:
                    book.available_copies = copies
                    book.update_status()
                return
        print("Book not found!")