'''
Online Shopping System
This program parses shopping data from a file to allow the user to pick items and quantities and then displays
these in a formatted receipt. The receipt is then stored in a file and uploaded to an S3 bucket.

Authors: Daniel Harris, Nicholas Hodder and Annette Clarke
'''
import os.path
from os import path

def user_file():
    f=open("products.dat","w")
    f.close()

def sample_file():
    f=open("products.dat","w")
    
    f.close()
    
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
            print(items)
    f.close()
    print(products)
    
    
    #for k,v in products.items():
     #   product_name = k
     #   for key, value in v.items():
      #      price = key
        #    quantity = value
      #      
    
if __name__ == "__main__":
    
    if not path.exists("products.dat"):
        file_choice = input("No products file found.\nType 'create' to make your own, or any other input (including blank) to use a sample file:  ")
        if file_choice.lower() == 'create':
            user_file()
        else:
            sample_file()
    
    get_products()













#product_name=input("What product would you like to purchase? ") #to distinquish from product in dictionary
#which may need this variable name
'''
if item not in the list print("Sorry! Invalid item. Please try again!!") 
if item present quantity=int(input("How many would you like to purchase?"))
He wants a line that says for ex. carrots cost$3.00. There are 20 left in stock. How many would you like to 
purchase?
    if quantity <0 or quantity >quantity in inventory:
        print("Sorry, that quantity is invalid. Please try again")
        continue
    ***  or could set up the above as if >0 and <inventory quantity then else would be the above but thats 
    not the way roy said.***
        
    (if valid quantity)
    else: 
        valid= input("Your total for this item was ${:.2f}. Is this ok? Y/N? ".format (item_total))
            if valid.lower()=='n':
                retry=input("Would you like to try again? Y/N)
                    if retry.lower()=='y':
                    continue
                    
                    elif retry.lower()=='n':
                        print("Your total for today was {:.2f}" .format(total))
                        break
                    
                    else:
                        print("Invalid entry! Please try again.)
                        continue
                
                
            elif valid.lower()=='y':
                cont=input("Would you like to continue? Y/N?)
                    if cont.lower()=='y':
                        continue
                    
                    elif cont.lower()=='n':
                        print("Your total for today was {:.2f}" .format(total))
                        break
                    
                    else:
                        print("Invalid entry! Please try again.)
                        continue
                
                
       
    
    
 item_total=price*quantity  these are all coming from the dictionary. but how???
 total=total + item_total
'''