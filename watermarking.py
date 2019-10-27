# importing the required modules 
from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2
import io, sys
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import re

#Usage: python3 watermarking.py "author_name" file_name
  
def add_watermark(wmFile, pageObj): 

    pageObj.mergePage(wmFile.getPage(0)) 
    return pageObj 
  
def main(): 

    f = sys.argv[1]
    origFileName = sys.argv[2]
    
    
    pdfFileObj = open(origFileName, 'rb') 
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    width, height = A4
    time = datetime.datetime.today()
    date = time.strftime("%h-%d-%Y %H:%M:%S")
    can.setFont("Times-Roman", 10)
    can.rotate(90)
    can.drawString(0.5*inch, -inch, '''Created by %s at Date: %s''' % ( f, date))
    can.save()
    packet.seek(0)
    mywatermark = PdfFileReader(packet)
        
    for page in range(pdfReader.numPages): 
        wmpageObj = add_watermark(mywatermark, pdfReader.getPage(page)) 
        pdfWriter.addPage(wmpageObj) 
    newFile = open(origFileName, 'wb') 
    pdfWriter.write(newFile) 
    pdfFileObj.close() 
    newFile.close() 
  
if __name__ == "__main__": 

    main() 
