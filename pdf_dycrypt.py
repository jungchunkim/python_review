# 암호걸린 PDF 파일 불러오기
import PyPDF2

pdfFile = open('encrypted.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

#값을 붙여넣을 빈 객체를 생성
pdfWriter = PyPDF2.PdfFileWriter()

# 암호를 입력하지 않으면 에러가 발생합니다.(암호:rosebud)
pdfReader.decrypt('rosebud')

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfReader.numPages

print(pdfReader.numPages,"페이지")

print("=======================================================")

pageObj = pdfReader.getPage(9)

pageObj.extractText()

print(pageObj.extractText())
