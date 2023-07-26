import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore",category=FutureWarning)
    from pyzbar.pyzbar import decode
   

import pymongo
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import numpy as np
import requests
from bs4 import BeautifulSoup
import json




cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while(True):
  success,img = cap.read()
  for barcode in decode(img):
    myData = barcode.data.decode('utf-8')
    pts = np.array([barcode.polygon],np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],True,(255,0,255),5)
    pts2 = barcode.rect
    cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
    code  = str(barcode.data)
    print(code)
    
  
  cv2.imshow("Result",img)
  cv2.waitKey(1)
  if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()

br = code.split('b')[1]

barcode = br[1:-1]
# barcode = str(barcode)
print("Barcode => " + barcode)




# Create a client to connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://admin:admin@nodeexpressprojects.tvkeh9h.mongodb.net/?retryWrites=true&w=majority")

# Get the database and collection objects
mydb = client["15-5"]
mycol = mydb["PDTS"]

# barcode_data = '8901491100519'
# code_aloe_vera = 8904109498923


# Fetch all the documents in the collection
query = { 'EAN Code':int(barcode)}


result = mycol.find_one(query)



if type(result) is type(None):
   barcode = str(barcode)
   print('No Entry Found in DataBase . . . \nGeting Data from Internet')
   lookup = "http://www.digit-eyes.com/cgi-bin/digiteyes.cgi?upcCode='"+barcode+"'&action=lookupUpc&go=Go%21#.ZEUlDM5ByUk"
   r = requests.get(lookup)
   soup = BeautifulSoup(r.content, 'html.parser')
   table = soup.find('script',attrs ={'type':'application/ld+json'})
   string = soup.find("td", {"id": "instructions"})
   print("Product Description =>  ")
   txt = string.text
   print(txt)

  #  print('Adding Data in DB for Future Refrence. . . .  \n')
   
   
  #  n = str(table)
  #  # print(n)
  #  n1 = n.split(">")
  #  n2 = n1[1].split("<")
  #  json_object = json.loads(n2[0])
  #  # print(json_object['name'])
   
  #  mydict = {
  #    "EAN Code": int(json_object['upc']),
  #    "Product Name":json_object['name'],
  #    "Product Description": json_object['description'],
  #    "Product Cost": None,
  #    "Product Ingredients": None
  #  }
   
   
  #  # print(mydict)
   
  #  client = pymongo.MongoClient("mongodb+srv://admin:admin@nodeexpressprojects.tvkeh9h.mongodb.net/?retryWrites=true&w=majority")
   
  #  # Get the database and collection objects
  #  mydb = client["15-5"]
  #  mycol = mydb["PDTS"]
   
  #  x = mycol.insert_one(mydict)
   
  #  # print(x)
  #  print("Inserted-Successfully")
   

else:
   print('Fetching Product Details From DB. . . .  \n')
   result = mycol.find_one(query)
  #  print(type(result))
   print(result['Product Description']) 
   

