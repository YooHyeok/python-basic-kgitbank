
from selenium import webdriver
import time

driver = webdriver.Chrome("d:/py1230/chromedriver.exe")
driver.get("http://www.naver.com")
driver.find_element_by_xpath('//*[@id="news_cast"]/div[1]/ul/li[1]/a').click()

# 
# # 1위 뉴스
# //*[@id="right.ranking_contents"]/ul/li[1]/a
# 
# # 2위뉴스
# //*[@id="right.ranking_contents"]/ul/li[2]/a
# 
# # 5위뉴스
# //*[@id="right.ranking_contents"]/ul/li[5]/a
# 
# # 10위뉴스
# //*[@id="right.ranking_contents"]/ul/li[10]/a


# for x in range(100,106): 
#     news_menu = driver.find_element_by_xpath('//*[@id="right.ranking_tab_%d"]' % x)
#     for n in range(1,6): 
#         news_rank = driver.find_element_by_xpath('//*[@id="right.ranking_contents"]/ul/li[%d]/a' % n)
#         news_menu.click()
#         news_rank.click()
#         time.sleep(0.8)
         
for x in range(6): 
    news_menu = '//*[@id="right.ranking_tab_%10d"]' % x
    for n in range(1,6): 
        news_rank = driver.find_element_by_xpath('//*[@id="right.ranking_contents"]/ul/li[%d]/a' % n)
        driver.find_element_by_xpath(news_menu).click()
        driver.find_element_by_xpath(news_rank).click()
        time.sleep(0.8)
        
    
    
    
    
# for n in range(1,11): #[1~10]
#     news_rank = driver.find_element_by_xpath('//*[@id="right.ranking_contents"]/ul/li[%d]/a' % n)
#     news_rank.click()
#     time.sleep(0.8)
    



















