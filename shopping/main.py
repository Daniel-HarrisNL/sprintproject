'''
Online Shopping System
This program parses shopping data from a file to allow the user to pick items and quantities and then displays
these in a formatted receipt. The receipt is then stored in a file and uploaded to an S3 bucket.

Authors: Daniel Harris, Nicholas Hodder and Annette Clarke
'''



#open file and parse data using :
'''

just trying out ways to get the data 

f=open("products.dat","r")
content=f.readline()
print(content)
content_list=content.split(":")
print(content_list)
price = 0
quantity = 0
newvalue = 0

products = {
                'chicken' :  {'price':price,'quantity':quantity},
                'pizza' :  {'price':price,'quantity':quantity}
    
    
    
}

for key,value in products.items():
    for k,v in value.items():
        #do some code...
        #to update the new values..
        v = newvalue
 '''     
''' The one below will bring back a nested dictionary or line items depending on how you print but don't know
how to assign the values to the variables we'll need
'''
f=open('products.dat')
products=dict()
for line in f:
    items=line.strip("\n").split(':')
    products.update({items[0]:dict()})
    number_of_items=len(items)
    for i in range(1,number_of_items-1,2):
        if items[0] in products.keys():
            products[items[0]].update({items[1]:items[i+1]})      
    
    
    
product_name=input("What product would you like to purchase? ") #to distinquish from product in dictionary
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