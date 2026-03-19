from datetime import datetime
import random
book_file="book.csv"
staff_file="staff.csv"
customer_file="customer.csv"
paid_histories_file="paid_histories.csv"
sale_histories_file="sale_histories.csv"
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
        self.read_data()
    def read_data(self):
        try:
            with open(book_file, "r", encoding="utf-8") as f:
                lines = f.readlines()[1:]
                for line in lines:
                    if not line.strip():
                        continue
                    items = line.strip().split(",")
                    book = Book(
                        items[0],  
                        items[1], 
                        items[2],  
                        items[3],  
                        int(items[6]),  
                        int(items[7]),  
                        items[8]   
                    )
                    book.available_copies = int(items[5])
                    book.status=items[4]
                    self.books.append(book)
            print(f"Loaded {len(self.books)} books")
        except FileNotFoundError:
            print("Book file not found!")
    def write_data(self):
        with open(book_file, "w", encoding="utf-8") as f:
            for book in self.books:
                f.write(
                    f"{book.book_id},{book.book_title},{book.category},"
                    f"{book.author},{book.selling_price},{book.import_price},"
                    f"{book.book_publisher},{book.available_copies}\n"
                )
    def add_book(self,book):
        book.update_status()
        self.books.append(book)
        self.write_data()
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.write_data()
                print("Book removed")
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
                self.write_data()
                print("Book updated")
                return
        print("Book not found!")
class Staff:
    def __init__(self, staff_id, name):
        self.staff_id = staff_id
        self.name = name
    def __str__(self):
        return f"{self.staff_id}, {self.name}"
class StaffManager:
    def __init__(self):
        super().__init__()
        self.listOfStaff = []
        self.current_staff = None
    def read_data(self):
        try:
            fread = open(staff_file, "r", encoding="utf-8")
            flines = fread.readlines()[1:]
            for line in flines:
                if not line.isspace():
                    line = line.strip()
                    items = line.split(",")
                    _id = items[0]
                    _name = items[1]
                    staff = Staff(_id, _name)
                    self.listOfStaff.append(staff)
            fread.close()
            print(f"Đã đọc {len(self.listOfStaff)} nhân viên từ file {staff_file}")
        except FileNotFoundError:
            print(f"Không tìm thấy file {staff_file}")
    def write_data(self):
        fwrite = open(staff_file, "w", encoding="utf-8")
        for staff in self.listOfStaff:
            fwrite.write(f"{staff.staff_id},{staff.name}\n")
        fwrite.close()
        print(f"Đã lưu {len(self.listOfStaff)} nhân viên vào file {staff_file}")
    def login(self, staff_id, name):
        for staff in self.listOfStaff:
            if staff.staff_id == staff_id and staff.name == name:
                self.current_staff = staff
                print(f"Đăng nhập thành công! Xin chào {staff.name}")
                return True
            print("Sai mã nhân viên hoặc tên!")
            return False
    def view_all_staff(self):
        if not self.listOfStaff:
            print("Chưa có nhân viên nào!")
            return

        print("\n=== DANH SÁCH NHÂN VIÊN ===")
        for staff in self.listOfStaff:
            print(f"{staff.staff_id},{staff.name}")
    def add_staff(self, staff_id, name):
        for staff in self.listOfStaff:
            if staff.staff_id == staff_id:
                print(f"Mã nhân viên {staff_id} đã tồn tại!")
                return False
        new_staff = Staff(staff_id, name)
        self.listOfStaff.append(new_staff)
        self.write_data()
        print(f"Đã thêm nhân viên {name} thành công!")
        return True
    def update_staff(self, staff_id, new_name=None):
        for staff in self.listOfStaff:
            if staff.staff_id == staff_id:
                if new_name:
                    staff.name = new_name
                self.write_data()
                print(f"Đã cập nhật nhân viên {staff_id} thành công!")
                return True
            print(f"Không tìm thấy nhân viên với mã {staff_id}")
            return False
    def delete_staff(self, staff_id):
        for i, staff in enumerate(self.listOfStaff):
            if staff.staff_id == staff_id:
                if self.current_staff and self.current_staff.staff_id == staff_id:
                    print("Không thể xóa tài khoản đang đăng nhập!")
                    return False
                del self.listOfStaff[i]
                self.write_data()
                print(f"Đã xóa nhân viên {staff_id} thành công!")
                return True
            print(f"Không tìm thấy nhân viên với mã {staff_id}")
            return False
    def find_staff(self, keyword):
        result = []
        keyword = keyword.strip().lower()
        for staff in self.listOfStaff:
            if (keyword in staff.staff_id.lower() or 
                keyword in staff.name.lower()):
                result.append(staff)
        return result

class Customer:
    def __init__(self, customer_name, customer_phone, customer_id):
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.customer_id = customer_id
    def __str__(self):
        return f"{self.customer_id}, {self.customer_name}, {self.customer_phone}"
class CustomerManager:
    def __init__(self, book_manager):
        self.book_manager = book_manager
        self.customers=[]
    def search_by_id(self, book_id):
        for book in self.book_manager.books:
            if book.book_id == book_id:
                print(book)
                return book
        print("Book not found")
        return None
    def search_by_price(self, price):
        found = False
        for book in self.book_manager.books:
            if book.selling_price == price:
                print(book)
                found = True
        if not found:
            print("No book found with that price")
            return
class Transaction:
    def __init__(self, customer, book, quantity, total_amount, date_time):
        self.customer=customer
        self.book=book
        self.quantity=quantity
        self.total_amount=total_amount
        self.date_time=date_time
    def __str__(self):
        return f"{self.customer} bought {self.book} x {self.quantity} = {self.total_amount} VND at {self.date_time}"
class TransactionManager:
    def __init__(self, book_manager):
        self.book_manager=book_manager
    def buy_book(self, customer, book_id, quantity):
        book=None
        for b in self.book_manager.books:
            if b.book_id==book_id:
                book=b
                break
        if book is None:
            print("Not found book")
            return
        if book.available_copies<quantity:
            print("Not have enough book")
            return
        total_amount=book.selling_price*quantity
        book.available_copies-=quantity
        book.update_status()
        now=datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        transaction=Transaction(customer, book, quantity, total_amount, now)
        self.save_paid_history(transaction)
        self.save_sale_history(transaction)
        self.book_manager.write_data()
        print("Buy book successfully")
        print(transaction)
    def save_paid_history(self, transaction):
        with open(paid_histories_file, "a", encoding="utf-8") as f:
            f.write(
                f"{transaction.customer.customer_id},"
                f"{transaction.book.book_id},"
                f"{transaction.total_amount},"
                f"{transaction.date_time}\n"
            )
    def save_sale_history(self, transaction):
        with open(sale_histories_file, "a", encoding="utf-8") as f:
            f.write(
                f"{transaction.customer.customer_id},"
                f"{transaction.customer.customer_name},"
                f"{transaction.book.book_id},"
                f"{transaction.book.book_title},"
                f"{transaction.total_amount},"
                f"{transaction.date_time}\n"
            )
    def view_paid_history(self, customer_id, quantity):
        try:
            with open(paid_histories_file, "r", encoding="utf-8") as f:
                found=False
                for line in f:
                    items=line.strip().split(",")
                    if items[0]==customer_id:
                        print(line.strip())
                        found=True
                if not found:
                    print("No paid history")
        except FileNotFoundError:
            print("File not found")
    def view_sale_history(self, book_id):
        try:
            with open(sale_histories_file, "r", encoding="utf-8") as f:
                found=False
                for line in f:
                    items=line.strip().split(",")
                    if items[0]==book_id:
                        print(line.strip())
                        found=True
                if not found:
                    print("No sale history")
        except FileNotFoundError:
            print("File not found")

def show_menu():
    print("1. Sign in as customer")
    print("2. Sign in as staff")
    print("3. Exist")
def staff_display(book_manager, transaction_manager):
    sn1=input("Enter name")
    found = False
    with open(staff_file, "r", encoding="utf-8") as f:
        for line in f:
            name = line.strip().split(",")[1]  
            if sn1 == name:
                found = True
                break
    if not found:
        print("Staff not found")
        return
    while True: 
        print("1. Search book")
        print("2. Adjust book")
        print("3. View Transaction")
        print("4. Back")
        c2=int(input("Choose: "))
        if c2==1:
            n=input("Enter book title: ").lower()
            for book in book_manager.books:
                if n in book.book_title.lower():
                    print(book)
        elif c2==2:
            book_id=input("Enter book id: ")
            price=input("New price (enter to skip): ")
            copies=input("New copies (enter to skip): ")
            price=float(price) if price else None
            copies=int(copies) if copies else None
            book_manager.update_book(book_id, price, copies)
            book_manager.write_data()      
        elif c2==3:
            b=input("Enter book ID: ")
            transaction_manager.view_sale_history(b)
        elif c2==4:
            break
        
def customer_display(book_manager, transaction_manager):
    cs1=input("Enter name: ")
    cs2=input("Enter phone: ")
    found_customer=None
    try:
        with open(customer_file, "r", encoding="utf-8") as f:
            for line in f:
                items=line.strip().split(",")
                if len(items)<=3:
                    continue
                c_id=items[0]
                c_name=items[1]
                c_phone=items[2]
                if cs1==c_name and cs2==c_phone:
                    found_customer=Customer(c_name, c_phone, c_id)
                    break
    except FileNotFoundError:
        pass
    if found_customer:
        customer=found_customer
        print("Customer found: ")
        print(customer)
    else:
        customer_id="C"+str(random.randint(100,999))
        customer=Customer(cs1, cs2, customer_id)
        with open(customer_file, "a", encoding="utf-8") as f:
            f.write(f"{cs1}, {cs2}, {customer_id}\n")
        print("New customer added")
        print(customer)
    while True:
        print("1. Search book")
        print("2. Buy book")
        print("3. Search paid history")
        print("4. Back")
        c2=int(input("Choose: "))
        if c2==1:
            n=input("Enter book title: ").lower()
            for book in book_manager.books:
                if n in book.book_title.lower():
                    print(book)           
        elif c2==2:
           book_id=input("Enter book id: ")
           quantity=int(input("Enter quantity: "))
           transaction_manager.buy_book(customer, book_id, quantity)
        elif c2==3:
            transaction_manager.view_paid_history(customer.customer_id)
        elif c2==4:
            break   

def main():
    book_manager=BookManager()
    transaction_manager=TransactionManager(book_manager)
    while True: 
        show_menu()
        choice=int(input("Choose: "))
        if choice==1:
            customer_display(book_manager, transaction_manager)
        elif choice==2:
            staff_display(book_manager, transaction_manager)
        elif choice==3:
            print("Goodbye")
            break
if __name__ == "__main__": 
    main()
            


