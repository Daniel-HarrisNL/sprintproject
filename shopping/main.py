'''
Online Shopping System
This program parses shopping data from a file to allow the user to pick items and quantities and then displays
these in a formatted receipt. The receipt is then stored in a file and uploaded to an S3 bucket.

Authors: Daniel Harris, Nicholas Hodder and Annette Clarke
'''
import os.path
from os import path

def add_products():
    f=open("products.dat","a")
    more_products = True
    while more_products == True:
        new_product = input("Enter product name to add to the file: ")
        new_product = new_product.strip()
        if not new_product.isalnum():
            print("Error: Product name must be alphanumeric.")
            continue
        while True:
            try:
                new_price = float(input("Enter the price of the product: $"))
            except:
                print("Error: Must only enter the price of the product, example: 9.99")
                continue
            break
        while True:
            try:
                new_quantity = int(input("Enter the quantity of the product available: "))
            except:
                print("Error: Must only enter the quantity of the product, example: 15")
                continue
            break
        
        f.write("{}:{}:{}\n".format(new_product.lower(),new_price,new_quantity))
        print("Product added!")
        again = input("Are there more products to add? 'Y' for yes, or any other input (including blank) to finish: ")
        if again.upper() == 'Y':
            continue
        else:
            more_products = False
            break
    f.close()
    return


def user_file():
    f=open("products.dat","w")
    f.close()
    add_products()
    print("User file has been created.")
    return


def purchase_item(products,receipt):
        while True:
            product_name = input("What product would you like to buy? ")
            product_name = product_name.strip()
            if product_name.lower() not in products:
                print("Error: Product entered is not available, please try again.")
                continue
            else:
                break
        price = [i for i in products[product_name].keys()][0]
        quantity = [i for i in products[product_name].values()][0]
        print("{} costs ${} per item. There are {} left in stock.".format(product_name, price,quantity))
        while True:
            try:
                number_purchased=int(input("How many would you like to purchase? Enter 0 to cancel: "))
            except:
                print("Error: Please enter an integer quantity.")
                continue
            if number_purchased == 0:
                print("Quantity 0 selected, cancelling product purchase.")
                break
            elif number_purchased < 0 or number_purchased > int(quantity):
                print("Sorry, that quantity is invalid. Please try again")
                continue
            item_total=float(price)*(number_purchased)
            confirm = input("Your total for this item is ${:.2f}. Enter any input (including blank) to confirm, or 'NO' to cancel this item.".format(item_total))
            if confirm.upper() == "NO":
                print("Please enter a new quantity. ")
                continue
            break
         
        #Iterate through products for the one being purchased
        if not number_purchased == 0:
            for k,v in products.items():
                if k == product_name:                
                    for key, value in v.items():
                        if key == "quantity":
                            #Update the quantity by subtracting the number purchased
                            v[key] = quantity - number_purchased
            if product_name in receipt:
                print("Updated old product quantity purchased with the new quantity.")
            receipt[product_name] = {'price':item_total,'quantity':number_purchased}
        return products, receipt
            
    
    
def sample_file():
    f=open("products.dat","w")
    f.write("frozen pizza:9.99:15\n")
    f.write("potatoes:6.97:20\n")
    f.write("chicken:10.99:15\n")
    f.write("orange juice:4.50:7\n")
    f.write("cheesestrings:6.58:10\n")
    f.write("lasagne:10.99:5\n")
    f.write("steak:26.99:6\n")
    f.write("beer:15.99:10\n")
    print("Sample file generated.")
    f.close()
    return
   
    
def get_products():
    f=open("products.dat")
    products=dict()
    for line in f:
        items=line.strip("\n").split(':')
        products.update({items[0]:dict()})
        number_of_items=len(items)
        for i in range(1,number_of_items-1,2):
            if items[0] in products.keys():
                products[items[0]].update({items[1]:items[i+1]})  
    f.close()
    return products
    
    
        
    
if __name__ == "__main__":
    #Check for 'products.dat' prompt for user made file, or sample file to be used in the program.
    if not path.exists("products.dat"):
        file_choice = input("No products file found.\nType 'create' to make your own, or any other input (including blank) to use a sample file:  ")
        if file_choice.lower() == 'create':
            user_file()
        else:
            sample_file()
    else:
        print("Found 'products.dat'.")
        
    
    products = get_products()
    
    print ("Hello! Welcome to Billy Bob's Bargain Bonanza! The products we have for sale are as follows:  \n\n")
    for product_name in products:
        print(product_name.upper() + ':')

        for price in products[product_name]:
            print ("Price: ${}".format (price))
        
        for quantity in products[product_name].values():
            print ("Quantity Remaining: {}\n".format(quantity))
            
    receipt = dict()
        
    while True:
        products, receipt = purchase_item(products, receipt)
        add_another = input("Enter 'MORE' to add purchase another product, or any other input (including blank) to stop: ")
        if add_another.upper() == 'MORE':
            continue
        else:
            break
        
    HST = 0.15
    subtotal = 0
    total = 0
    
    #Print the receipt
    print("RECEIPT\n\n")
    #Try to get this to print on one line
    for product_name in receipt:
        print(product_name.upper() + ':')

        for price in receipt[product_name]:
            print ("Price: ${}".format (price))
        
        for quantity in receipt[product_name].values():
            print ("Quantity Remaining: {}\n".format(quantity))
    
    
    
   # for k,v in receipt.items():
    #    for key,value in v.items():
    #        if key == 'price':
      #          item_price = value
       #         subtotal = subtotal + item_price
       #     elif key == 'quantity':
      #          item_quantity = value
      #  print("{} * {} {}\n".format(key.upper(), item_quantity, item_price))
     #   
  #  print("SUBTOTAL: ${}".format)
            
    
        

    
    
    