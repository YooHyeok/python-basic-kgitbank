
# 셀레늄: 웹 자동화 및 웹의 소스코드를 수집하는 모듈
# 셀레늄 임포트.
from selenium import webdriver
import time 

# 크롬 물리드라이버 가동 명령.
driver = webdriver.Chrome('d:/py1230/chromedriver.exe')

# 물리드라이버로 사이트 이동 명령
driver.get("https://www.naver.com")
time.sleep(2)

# # 자동으로 버튼이나 링크 클릭 제어하기.
# login_btn = driver.find_element_by_xpath('//*[@id="account"]/div/a/i')
# login_btn.click()
# 
# # 자동으로 텍스트 입력하기
# time.sleep(1.5)
# id_input = driver.find_element_by_xpath('//*[@id="id"]')
# id_input.send_keys("abc1234")
# 
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="pw"]').send_keys('aaa1111')
# 
# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# 검색창에 손흥민을 검색해 보세요. (webdriver 객체를 활용)
search_input = driver.find_element_by_xpath('//*[@id="query"]')
search_input.send_keys("손흥민")
time.sleep(1.5)
search_btn = driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]')
search_btn.click()















