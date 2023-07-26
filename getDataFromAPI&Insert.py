import pymongo
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import numpy as np
import requests
from bs4 import BeautifulSoup
import json
from random import *



code='8902519009807'

        

lookup = "http://www.digit-eyes.com/cgi-bin/digiteyes.cgi?upcCode="+code+"&action=lookupUpc&go=Go%21#.ZEUlDM5ByUk"
r = requests.get(lookup)
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find('script',attrs ={'type':'application/ld+json'})
string = soup.find("td", {"id": "instructions"})
# print(string)
# print("Product Description =>  ")
txt = string
# print(string.text)
n = str(table)
# print(n)
n1 = n.split(">")
n2 = n1[1].split("<")
json_object = json.loads(n2[0])
# print(json_object['name'])

mydict = {
  "EAN Code": int(json_object['upc']),
  "Product Name":json_object['name'],
  "Product Description": json_object['description'],
  "Product Cost": randint(25, 100),
  "Product Ingredients": None
}

print(mydict)

# mydict = {
#   "EAN Code": '8964000090664',
#   "Product Name":'Pears Soap',
#   "Product Description": 'Cleaning With Moisturization',
#   "Product Cost": None,
#   "Product Ingredients": None
# }


# # print(mydict)

client = pymongo.MongoClient(key)

# Get the database and collection objects
mydb = client["15-5"]
mycol = mydb["PDTS"]

x = mycol.insert_one(mydict)

# print(x)
print("Inserted-successfully")
