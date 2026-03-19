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

def show_menu():
    print("1. Sign in as customer")
    print("2. Sign in as staff")
    print("3. Exsist")
def staff_display():
    sn1=input("Enter name")
    found = False
    with open("staff.csv", "r") as f:
        for line in f:
            name = line.strip().split(",")[1]  
            if sn1 == name:
                found = True
                break
        if found==False:
            print("Staff not found")
            return
    if found==True:
        print("1. Search book")
        print("2. Adjust book")
        print("3. View Transaction")
        c2=int(input(""))
        if c2==1:
            b=input("Enter book name: ")
            with open("book.csv", "r") as f:
                found = False
                for line in f:
                    data = line.strip().split(",")
                    
                    pm = Book(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[6],
                        data[7],
                        data[8]
                    )
                    if b == pm.book_title:
                        print("Book found:")
                        print(pm)
                        found = True
                        break
                if not found:
                    print("Book not found")
show_menu()
staff_display()