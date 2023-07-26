import pymongo
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import numpy as np
import requests
from bs4 import BeautifulSoup

# code_aloe_vera = 8904109498923

client = pymongo.MongoClient("mongodb+srv://admin:admin@nodeexpressprojects.tvkeh9h.mongodb.net/?retryWrites=true&w=majority")

# Get the database and collection objects
mydb = client["15-5"]
mycol = mydb["PDTS"]

barcode = 8901262201001

# query = { 'EAN Code':int(8904109498923)}

# aloevera
query = { 'EAN Code':int(barcode)}
result1 = mycol.find_one(query)
query = { 'EAN Code':str(barcode)}

result2 = mycol.find_one(query)

print('Fetching Product Details. . . .  \n')
# print(type(result))
print(result2['Product Description'])
