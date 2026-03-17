from datetime import datetime

# Simple Object
# Use public attributes to access easily
class Product: 
    def __init__(self,p_code,p_name,p_unit_price,p_amount_in_stock,p_expired_month,p_date,p_status):
        self.p_code = p_code
        self.p_name = p_name
        self.p_unit_price=p_unit_price
        self.p_amount_in_stock=p_amount_in_stock
        self.p_expired_month=p_expired_month
        self.p_date=p_date
        self.p_status=p_status
    def total_in_stock(self):
        return self.p_unit_price*self.p_amount_in_stock
    def remain_valid_month(self):
        day_difference = (datetime.today() - self.p_date).days
        month_diff = self.p_expired_month - day_difference/30
        return month_diff
    def is_valid(self):
        if self.remain_valid_month() > 0:
            return True
        else:
            return False

# Management Object
class ProductManager:
    def __init__(self):
        self.listOfProducts = []
    def read_data(self,file_name):
        fread = open(file_name)
        flines = fread.readlines()
        for line in flines:
          if not line.isspace():
            line = line.strip()
            items = line.split(',')
            
            _code = items[0]
            _name = items[1]
            _price = float(items[2])
            _amount = int(items[3])
            _months = int(items[4])
            _date = datetime.strptime(items[5], "%d-%m-%Y").date()
            _status = True
            if items[6] == 'unavailable':
                _status = False
            
            sp = Product(_code,_name,_price,_amount,_months,_date,_status)
            self.listOfProducts.append(sp)
            
        fread.close()
    def find_products(self,search_name):
        result = []
        search_name = search_name.strip()
        for item in self.listOfProducts:
            if search_name.upper() in item.p_name.upper():
                result.append(item)
        return result
    
    def calculate_product_in_stock(self):
        s = 0
        
        for item in self.listOfProducts:
            s = s + item.total_in_stock()
        
        return s
    
    def display_available_product_in_stock(self):
        # Tạo hàm lấy giá trị thuộc tính p_amount_in_stock để so sánh khi sắp xếp
        def compAmountInStock(x):
            return x.p_amount_in_stock
        
        # Lấy danh sách các sản phẩm còn kinh doanh
        available_list = []
        
        for p in self.listOfProducts:
            if p.p_status == True:
                available_list.append(p)
        
        # Sắp xếp danh sách tăng dần theo giá trị p_amount_in_stock
        available_list.sort(key=compAmountInStock)
        
        # Hiển thị các giá trị phần tử trong danh sách sau khi sắp xếp
        for p in available_list:
            print(p.p_code+','+p.p_name+','+str(p.p_unit_price)+','+str(p.p_amount_in_stock))

# Support function to show menu
def show_menu():
    print("\n")
    print("=====*****=====")
    print("Product Management Software")
    print("Type 1: Find product by name")
    print("Type 2: Calculate total in stock")
    print("Type 3: Display and sort available products in stock by amount_in_stock")
    print("Other: Exit App")
    print("=====*****=====")
    
# Main program
def main():
    
    pm = ProductManager()
    pm.read_data('data.csv')
    
    while(True):
        show_menu()
        
        tc = int(input("Your choice: "))
        if(tc == 1):
            sname = input('Type product name: ')
            print("Your result")
            kq = pm.find_products(sname)
            for item in kq:
                print(item.p_code+','+item.p_name+','+str(item.p_amount_in_stock))
        if(tc == 2):
            print("Your result")
            kq = pm.calculate_product_in_stock()
            print(kq)
        if(tc == 3):
            print("Your result")
            pm.display_available_product_in_stock()
        
        if(tc > 3):
            print("Bye bye")
            break;
#--------------------------------

# Entry point to run program
if __name__ == "__main__":
    main()






