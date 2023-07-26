from pyzbar.pyzbar import decode
import cv2
import numpy as np
import requests
from bs4 import BeautifulSoup

cap = cv2.VideoCapture(1)
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

barcode = code.split('b')[1]

print("Barcode = >" + barcode)
