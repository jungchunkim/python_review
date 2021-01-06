# PDF 파일에서 텍스트 불러오기

# PyPDF2 모듈을 가져온다.
import PyPDF2
import sys

#input_file = sys.argv[1]

# meetingminutes(회의록) PDF 파일을 바이너리 읽기모드로 열어서 pdfFileObj에 저장한다.
pdfFileObj = open('meetingminutes.pdf', 'rb')
# pdfFileObj = open(sys.argv[1], 'rb')

# PdfFileReader 객체를 pdfReader에 저장한다.
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# 문서에 있는 페이지의 총 개수는 PdfFileReader 객체의 numPages 속성에 저장된다.
# 문서에 있는 전체 페이지의 숫자가 출력된다.(meetingminutes.pdf는 전체 19페이지이다)
pdfReader.numPages

# meetingminutes(회의록) PDF 파일에는 여러 페이지가 있는데,
# 이중 첫 페이지에 있는 텍스트만 추출해본다.
pageObj = pdfReader.getPage(0)

# Page 객체를 얻었으면 텍스트 문자열을 돌려주는 extractText() 메소드를 호출한다.
pageObj.extractText()

# print() 함수를 사용하면 좀 더 깔끔한 내용으로 확인할 수 있다.
print(pageObj.extractText())










