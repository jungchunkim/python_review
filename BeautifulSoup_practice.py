#네이버 금융사이트에서 오늘의 달러환율 출력
from bs4 import BeautifulSoup
import urllib.request as req

#네이버 검색창에 환율검색 후 이동 -> 웹주소 복사

url="https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"

res=req.urlopen(url)

soup=BeautifulSoup(res, "html.parser")

price=soup.select_one("div.head_info > span.value").string
print("usd/krw = ", price)
