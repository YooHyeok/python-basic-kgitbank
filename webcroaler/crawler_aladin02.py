

from selenium import webdriver
import time
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

src = driver.page_source


html_s = BeautifulSoup(src, 'html.parser')


bs_div = html_s.find_all("div", class_="ss_book_box")

rank = 1


for bs in bs_div:
    
    first_book = bs.find_all("li")
   
    
    if first_book[0].text[0] == "[":
        book_title = first_book[1].text
        book_author = first_book[2].text
        book_price = first_book[3].text
        
    else:
        book_title = first_book[0].text
        book_author = first_book[1].text
        book_price = first_book[2].text
        
    info = book_author.split("|")       
    print(info)    

    f.write("# 순위: %d위\r\n" % rank)
    f.write("# 제목: " + book_title + "\r\n")
    f.write("# 저자: " + info[0].strip() + "\r\n")
    f.write("# 출판사: " + info[1].strip() + "\r\n")
    f.write("# 출판일: " + info[2].strip() + "\r\n")
    f.write("# 가격: " + book_price + "\r\n")
    f.write("-" * 50 + "\r\n")
    rank += 1

f.close()
































