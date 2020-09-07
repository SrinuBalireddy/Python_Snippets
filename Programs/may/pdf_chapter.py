# Write your code here :-)
import PyPDF2

pdfFileObj = open('SrinuBalireddy_CV.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
print(pageObj)
print(pageObj.extractText())
pdfFileObj.close()
