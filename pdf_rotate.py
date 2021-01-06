# 화면이 다른 출력물을 페이지 회전하여 올바르게 정의합니다.

import PyPDF2    

minutesFile = open('C:/Users/Python/Desktop/share/파이썬_PDF/rotatedPage.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(minutesFile)

page = pdfReader.getPage(0)

# 페이지 회전은 90도, 180도, 270도와 각각 양수/마이너스값만 사용할 수 있습니다.
page.rotateClockwise(-90)

pdfWriter = PyPDF2.PdfFileWriter()

pdfWriter.addPage(page)

resultPdfFile = open('C:/Users/Python/Desktop/share/파이썬_PDF/rotatedPage1.pdf', 'wb')

pdfWriter.write(resultPdfFile)

resultPdfFile.close()

minutesFile.close()
