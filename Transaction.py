from datetime import datetime
class Transaction:
    def __init__(self, total_amount):
        

class TransactionManager:
    pass

def show_menu():
    print("1. Sign in as customer")
    print("2. Sign in as staff")
    print("3. Exsist")

def staff_display(sn1):
    sn1=input("Enter name")
    if sn1 in staff.csv:
        print("1. Search book")
        print("2. Adjust book")
        print("3. View Transaction")
        c2=int(input(""))
        if c2==1:

        if c2==2:

        if c2==3:
        
def customer_display():
    cs1=input("Enter name:")
    if cs1 not in customer.csv:
        customer.csv.append(cs1)
    while cs1 in customer.csv:
        print("1. Search book")
        print("2. Buy book")
        print("3. Search paid history")
        c2=int(input(""))
        if c2==1:

        if c2==2:

        if c2==2:


def main():
    
    while True:
        show_menu()
        choice=int(input(""))
        if choice==1:
            customer_display()
        elif choice==2:
            staff_display()

            


