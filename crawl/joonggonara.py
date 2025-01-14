from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
import time
import pyperclip
import datetime
import pandas as pd
import random
import time 
import pandas as pd 
import os 
import pymysql 
import re 
from selenium import webdriver # pip install selenium 
from bs4 import BeautifulSoup as bs # pip install bs4
from selenium.common.exceptions import NoSuchElementException





def insert(curs, data):
    try: 
        sql = """insert into articles3(site_name, article_url, title,  price, image, published_at, crawled_at)
                        values (%s, %s, %s, %s, %s, %s, %s)"""

        curs.execute(sql, (data['site_name'],  data['article_url'], data['title'], 
                           data['price'], data['image'], data['published_at'], data['crawled_at']))
        conn.commit()

    except:
        raise
        print("==========")
        print("Fail")
        print("==========")

def nara(category, curs) :

    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(3)
    ENTER='/ue007'

    # 에러시 부여할 딜레이(단위[초])

    login=1

    # datetime
    now = datetime.datetime.now()
    today = now.strftime('%Y-%m-%d')

    # 엑셀
    wb = Workbook(write_only=True)
    ws = wb.create_sheet(today)
    ws.append(['사이트 이름', '글 url', '제목', '가격', '이미지', '작성일', '크롤링한 날짜'])

    if login==1 :
        # 로그인
        driver.get('https://nid.naver.com/nidlogin.login')
        time.sleep(1)

        pyperclip.copy('') # 네이버 ID를 복붙하여 넣음
        driver.find_element_by_id('id').send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        pyperclip.copy('') # 네이버 PW를 복붙하여 넣음
        driver.find_element_by_id('pw').send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        driver.find_element_by_id('log.login').click()
        time.sleep(1)

    url = 'https://cafe.naver.com/joonggonara' # 크롤링 할 카페 주소
    driver.get(url)


    total_list =[]
    for i in range(200): 
        pg = str(i+1)
        addr = f'https://cafe.naver.com/ArticleList.nhn?search.clubid=10050146&search.menuid={category}&search.boardtype=I&search.totalCount=201&search.cafeId=10050146&search.page='+pg
        driver.get(addr)
        driver.switch_to.frame('cafe_main')
        html = driver.page_source
        soup= bs(html, 'html.parser')
        title_list = soup.findAll("a",{"class":"tit"}) # 게시글 제목
        date_list = soup.findAll("span",{"class":"date"}) # 게시글 작성 날짜
        price_list = soup.findAll("dd",{"class":"price"}) # 제품 가격
        image_list = soup.findAll("a",{"class":"album-img"}) # 제품 사진

    

        for a, b, c, d in zip(title_list, date_list, price_list, image_list):
            data = {}
            list=[]
            crawled_at = time.strftime('%Y-%m-%d %H:%M:%S')
            #list.append('junggo')
            #list.append(a.text.strip()) # title
            #list.append(b.text) # published_at
            #list.append(c.text) # price
            #list.append(d.img.attrs['src']) # image
            #list.append('https://cafe.naver.com'+a.attrs['href']) # url
            #list.append(crawled_at)
            #total_list.append(list)
            #time.sleep(delay)
            
            data['site_name'] = "중고나라"
            data['article_url'] = 'https://cafe.naver.com'+a.attrs['href']
            data['title'] = a.text.strip()
            data['price'] = c.text.strip('원').replace(',',"")
            data['image'] = d.img.attrs['src']
            data['published_at'] = b.text
            data['crawled_at'] = crawled_at
            total_list.append(data)
            """ 데이터베이스에 Insert """
            insert(curs, data)
            

        print("page "+ str(i+1))
        
        # # 엑셀에 작성
        # ws.append(data['site_name'],  data['article_url'], data['title'], data['price'], data['image'], data['published_at'], data['crawled_at'])

    # 끝내고 엑셀 파일 저장
    driver.close()
    wb.save(f'중고나라 {today} 매물.xlsx')

    # 데이터프레임 생성
    df = pd.read_excel(f'중고나라 {today} 매물.xlsx')
    
#print(df.describe())

conn = pymysql.connect(
    user='root', 
    passwd='', #패스워드 입력
    host='127.0.0.1', 
    db='testdb', 
    charset='utf8'
 )


conn.set_charset('utf8mb4')

curs = conn.cursor()

'''
334 : 노트북
382 : 데스크탑
385 : PC 주요부품
2314 : 출산/육아 코너마켓(공용)
333 : 출산/임부용품
376 : 유아/아동용품
1322 : 중고차-현대/제네시스
1323 : 중고차-기아
1324 : 중고차-쉐보레/대우
2054 : 계절가전
452 : 생활가전
451 : 주방가전
346 : 드릴/전동공구
489 : 에어/유압공구
486 : 공구/공구함
1156 : 모바일 상품권
1866 : 식음료 상품권/쿠폰
1285 : 영화/연극/공연
530 : 텐트/타프/매트
2103 : 캠핑 테이블/의자/가구
332 : 여성 기초 화장품
370 : 남성 화장품
372 : 향수
344 : 침실가구
470 : 거실가구
471 : 주방가구
367 : 여성 악세서리
1096 : 남성 악세서리
432 : MTB/사이클
1473 : 픽시/하이브리드
1474 : 전기/특수자전거
338 : 닌텐도/WII
419 : 플레이스테이션
420 : XBOX
457 : 미술용품도구
751 : 악기
414 : LP/DVD/음반
1432 : 드라이버/우드
1434 : 아이언/퍼터
782 : 명품가방
1007 : 명품 여성 의류
1008 : 명품 남성 의류
356 : 여성 의류
331 : 여성 신발
358 : 남성 의류
363 : 남성 신발
754 : 여행/숙박 티켓
436 : 등산 용품
439 : 낚시 용품
335 : DSLR
396 : 필름/중형카메라
398 : 삼각대/풀래시/조명
340 : 축구용품/의류
430 : 야구용품/의류
431 : 농구용품/의류
450 : 욕실/주방 용품
444 : 문구/사무 용품
446 : 강아지/고양이 용품
1155 : 굿즈/보드게임
'''

category = [334, 382, 385, 1322,1323,1324,2054,452,451,346,489,486,1156,1866,1285,530,2103,332,370,372,344,470,471,367,1096,432,1473,1474,338,419,420,457,751,414,1432,1434,782,1007,1008,356,331,358,363,754,436,439,335,396,398,340]

all_list =[]
for i in category:
    nara(i, curs)


#print("start")
#nara(category, curs)

#print("finish")
#conn.close()
#driver.quit()