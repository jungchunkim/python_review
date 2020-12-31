import webbrowser


'''
naver_search_url="https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query="
daum_search_url="https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q="
nate_search_url="https://search.daum.net/nate?thr=sbma&w=tot&q="
google_search_url="www.google.com/#q="
search_word=['이천 반도체', '이천 쌀', '이천 도자기', '이천 복숭아']

for search in search_word:
    webbrowser.open_new(naver_search_url+search)
'''


naver_search_url="https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query="
daum_search_url="https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q="
nate_search_url="https://search.daum.net/nate?thr=sbma&w=tot&q="
google_search_url="www.google.com/#q="

search_word=['이천 반도체', '이천 쌀', '이천 도자기', '이천 복숭아']

urls=["https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query="\
,"https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q=",\
  "https://search.daum.net/nate?thr=sbma&w=tot&q=", \
 "www.google.com/#q="     ]

i=0

for url in urls:
    for word in search_word:
        if search_word[i]==word:
            webbrowser.open_new(url+word)
    i+=1
