# importing the required modules 
from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2
import io
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import re
  
def add_watermark(wmFile, pageObj): 

    pageObj.mergePage(wmFile.getPage(0)) 
    return pageObj 
  
def main(): 
    
#    origFileName = 'merged_output.pdf'
    origFileName = 'Chapter_1.pdf' 
    newFileName = 'output.pdf'
    
    pdfFileObj = open(origFileName, 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    text = pdfReader.getPage(0).extractText()
#    print(text)
    x = re.sub("\n+", "", text)
#    print(x)
    searchObj = re.search( r'BY.*THESIS', x, re.I)
    if searchObj:
        extracted_string = searchObj.group()
#       print(extracted_string)
        author = re.sub(r'BY', "", extracted_string)
#       print(author)
        author = re.sub(r'B.E. THESIS', "", author)
#       print(author)
        author = re.sub(r'\s{2,10}', "",author)
#       print(author)
        pdfWriter = PyPDF2.PdfFileWriter()
        packet = io.BytesIO()
        can = canvas.Canvas("./watermark.pdf", pagesize=A4)
        width, height = A4
        time = datetime.datetime.today()
        date = time.strftime("%h-%d-%Y %H:%M:%S")
        can.setFont("Times-Roman", 12)
        can.rotate(90)
        can.drawString(0.5*inch, -inch, '''Created by %s at Date: %s''' % ( author, date))
        can.save()
        packet.seek(0)
        mywatermark = PdfFileReader("watermark.pdf")
        
    else:
        pdfWriter = PyPDF2.PdfFileWriter()
        packet = io.BytesIO()
        can = canvas.Canvas("./watermark.pdf", pagesize=A4)
        width, height = A4
        time = datetime.datetime.today()
        date = time.strftime("%h-%d-%Y %H:%M:%S")
        can.setFont("Times-Roman", 12)
        can.rotate(90)
        can.drawString(0.5*inch, -inch, '''Created at Date: %s''' % (date))
        can.save()
        packet.seek(0)
        mywatermark = PdfFileReader("watermark.pdf")               
     
    for page in range(pdfReader.numPages): 
        wmpageObj = add_watermark(mywatermark, pdfReader.getPage(page)) 
        pdfWriter.addPage(wmpageObj) 
    newFile = open(newFileName, 'wb') 
    pdfWriter.write(newFile) 
    pdfFileObj.close() 
    newFile.close() 
  
if __name__ == "__main__": 

    main() 
