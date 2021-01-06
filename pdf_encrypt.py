#암호걸린 PDF 파일을 새로운 암호 지정하기
import PyPDF2

pdfFile = open('encrypted.pdf', 'rb')
pdfReader= PyPDF2.PdfFileReader(pdfFile)
pdfWriter=PyPDF2.PdfFileWriter()

#현재 사용중인 암호를 적어줍니다.
pdfReader.decrypt('rosebud')

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

#새로운 암호를 적어줍니다.
pdfWriter.encrypt('hongik')
resultPdf= open('encrypted2.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()
print('작업이 완료되었습니다.')
