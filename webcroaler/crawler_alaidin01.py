

from selenium import webdriver
import time
# 뷰티풀수프 임포트
from bs4 import BeautifulSoup
import codecs

file_path = "D:/py1230/알라딘 베스트셀러 1~50위.txt"

try:
    f = codecs.open(file_path, mode="w", encoding="utf-8")
    
except:
    print("디렉토리 경로를 찾을 수 없습니다.")




driver = webdriver.Chrome("D:/py1230/chromedriver.exe")
driver.get("https://www.aladin.co.kr")

driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

# selenium으로 현재 페이지의 html 소스코드를 전부 불러오기.
src = driver.page_source
# print(src)

# 뷰티풀수프 객체 생성
html_s = BeautifulSoup(src, 'html.parser')

'''
- 뷰티풀수프를 사용하여 수집하고 싶은 데이터가 들어있는
 태그를 부분 추출할 수 있습니다.
 
- find_all()메서드는 인수값으로 추출하고자 하는 태그의 
 이름을 적으면 해당 태그만 전부 추출하여 리스트에 담아 리턴합니다.
'''
bs_div = html_s.find_all("div", class_="ss_book_box")
# print("bs_div에 들어있는 데이터의 수:", len(bs_div))

# print(bs_div[0])

for bs in bs_div:
    
    first_book = bs.find_all("li")
    # print(first_book)
    
    #html태그 내의 텍스트만 추출하는 방법.
    
    if first_book[0].text[0] == "[":
        book_title = first_book[1].text
        book_author = first_book[2].text
        book_price = first_book[3].text
    else:
        book_title = first_book[0].text
        book_author = first_book[1].text
        book_price = first_book[2].text
    
    print()
    print()
    f.write("# 제목: " + book_title)
    f.write("# 저자: " + book_author)
    f.write("# 가격: " + book_price)




