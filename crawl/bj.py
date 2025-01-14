from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
import pandas as pd
import random
import pandas as pd 
import pymysql
import time
from selenium import webdriver # pip install selenium 
from bs4 import BeautifulSoup as bs # pip install bs4
from selenium.common.exceptions import NoSuchElementException


def insert(curs, data):
    try: 
        sql = """insert into articles(site_name,  article_url, title,  price, image, published_at, crawled_at)
                        values (%s, %s, %s, %s, %s, %s, %s)"""

        curs.execute(sql, (data['site_name'],  data['article_url'], data['title'], 
                        data['price'], data['image'], data['published_at'], data['crawled_at']))
        conn.commit()

    except:
        """print("==========")
        print("Fail")
        print("==========")"""

def crawlingbunjang(category, curs):
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    # to supress the error messages/logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options,executable_path=r"chromedriver.exe")
    driver.implicitly_wait(1)
    ENTER='/ue007'

    # 에러시 부여할 딜레이(단위[초])
    delay = random.random()



    url = 'https://m.bunjang.co.kr/' # 크롤링 할 카페 주소
    driver.get(url)

    total_list =[]
    for i in range(100): # 한 카테고리당 몇페이지 돌릴지
        pg = str(i+1)
        addr = f'https://m.bunjang.co.kr/categories/{category}?order=date&page='+pg
        driver.get(addr)
        html = driver.page_source
        soup= bs(html, 'html.parser')
        title_list = soup.findAll("div",{"class":"sc-chbbiW hmkmpv"})
        date_list = soup.findAll("div",{"class":"sc-gmeYpB fxEeIU"})
        price_list = soup.findAll("div",{"class":"sc-kxynE kwIxAx"})
        url_list = soup.findAll("a", {"class":"sc-LKuAh hjcqIZ"})
        img_list = soup.findAll("img", {"alt":"상품 이미지"})

        for a, b, c, d, e in zip(title_list, price_list, url_list, img_list, date_list):
            data = {}
            # list=[]
            # list.append(a.text)
            # list.append(b.text)
            # list.append('https://m.bunjang.co.kr'+c.attrs['href'])
            # list.append(d.attrs['src'])
            
            # list.append(e.span)
            # total_list.append(list)
            crawled_at = time.strftime('%Y-%m-%d %H:%M:%S')
            data['site_name'] = "bunjang"
            data['article_url'] ='https://m.bunjang.co.kr'+c.attrs['href']
            data['title'] = a.text
            data['price'] = b.text
            data['image'] = d.attrs['src']
            data['published_at'] = e.string
            data['crawled_at'] = crawled_at
            """ 데이터베이스에 Insert """
            insert(curs, data)
        

        print("page "+ str(i+1))
    
    driver.close()
    return total_list





conn = pymysql.connect(
    user='root', 
    passwd=' ', #자기 비밀번호
    host='127.0.0.1', 
    db='testdb', 
    charset='utf8'
 )

conn.set_charset('utf8mb4')

    # conn = pymysql.connect(host='127.0.0.1',  user='root',
    #                        password='pw', db='price', charset='utf8mb4', )

curs = conn.cursor()



"""
310 - 여성의류
320 - 남성의류
405 - 신발
430 - 가방
420 - 신발, 쥬얼리
400 - 패션 악세서리
600 - 디지털 가전
700 - 스포츠/레저
750 - 차량/오토바이
910 - 스타굿즈
930 - 키덜트
990 - 예술,희귀,수집품
920 - 음반/악기
900 - 도서/티켓/문구
410 - 뷰티/미용
810 - 가구/인테리어
800 - 생활/가공식품
500 - 유아동/출산
980 - 반려동물용품
999 - 기타

"""
# category=[310, 320, 405, 430, 420, 400, 600, 700, 750, 910, 930, 
# 990, 920, 900, 410, 810, 800, 500, 980, 999]

category=[930, 990, 920, 900, 410, 810, 800, 500, 980, 999]

all_list =[]
for i in category:
    crawlingbunjang(i, curs)
    # total_list=crawlingbunjang(i, curs)
    # for j in total_list:
    #     all_list.append(j)


# print(pd.DataFrame(all_list))

