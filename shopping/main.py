'''
Online Shopping System
This program parses shopping data from a file to allow the user to pick items and quantities and then displays
these in a formatted receipt. The receipt is then stored in a file and uploaded to an S3 bucket.

Authors: Daniel Harris, Nicholas Hodder and Annette Clarke
'''



#open file and parse data using :
f=open("products.dat","r")
content=f.readline()
print(content)
content_list=content.split(":")
print(content_list)