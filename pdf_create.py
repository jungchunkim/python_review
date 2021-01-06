# 두개의 파일을 통합하여 새로운 파일로 저장합니다.
import PyPDF2

# 두개의 파일을 호출합니다.
pdf1File = open('d:/meetingminutes.pdf', 'rb')
pdf2File = open('d:/meetingminutes2.pdf', 'rb')    

# 각각의 파일을 읽어들여 저장합니다.
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter() 

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# 새로운 이름으로 저장합니다.
pdfOutputFile = open('C:/Users/Python/Desktop/share/파이썬_PDFcombined.pdf', 'wb')

pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()

pdf1File.close()
pdf2File.close()

print("작업이 완료되었습니다")







