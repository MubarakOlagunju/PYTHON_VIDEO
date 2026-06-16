#DIGITAL ARCHIVE SYSTEM

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
        
    def accept_info(self):
        print(f"Productname: {self.name}, Price: {self.price}")

productname = input("Enter product name: ")
productprice = input("Enter product price: ")

product1 = Product(productname, productprice)

product1.accept_info()

file = open("inventory.txt", "a")
file.write(f"\nProductname: {product1.name}, Price: {product1.price}")
file.close()
print("Data saved successfully....")