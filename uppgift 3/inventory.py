import csv
import os
import locale


def load_data(filename):
    global products 
    products = [] 
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    
def get_product_by_id(product_id):
    for product in products:
        if product['id'] == product:
            return product 

def get_products(products):
    product_list = []
    for product in products:
        product_info = f"{product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)
    
    return "\n".join(product_list)

def add_product():
    id = max(product['id']for product in products)
    name = input("Namn på produkten: ")
    desc = input("Beskriv produkten: ")
    price = float(input("Priset på produkten: "))
    quantity = int(input("Produkt kvantitet: "))
    print(add_product)

id = int(input("vilken produkt vill du visa: "))


#TODO: gör om så du slipper använda global-keyword (flytta inte "product = []")
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')
load_data('db_products.csv')

print(get_products(products))