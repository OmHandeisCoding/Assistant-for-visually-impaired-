from pyzbar.pyzbar import decode
from PIL import Image
import pymongo

img = Image.open(r'C:\Users\91726\Desktop\FinalDemonstration\Barcode-AloeVera.jpeg')

barcodes = decode(img)

for barcode in barcodes:
    barcode_data = barcode.data.decode('utf-8')
    print(barcode_data)


