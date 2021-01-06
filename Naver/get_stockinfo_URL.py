"""
   종목 list의 모든 종목 코드에 대해서 재무재표 정보가 있는 URL 을 얻어와서 저장함.
"""
import time
import random
import pandas as pd
from selenium import webdriver
from collections import OrderedDict

columns = ['종목코드','종목명','dataURL','재무재표컬럼','재무재표데이터']
dataContainer = [[],[],[],[],[]]
data = OrderedDict(list(zip(columns,dataContainer)))

path = "D:\\chromedriver.exe"
driver = webdriver.Chrome(path)

# 모든 종목코드를 읽음
item_df = pd.read_csv("D:\\PyQt5_Sample\\Naver\\종목.csv")

item_codes = item_df['종목코드'].to_list()
item_names = item_df['종목명'].to_list()

# 종목페이지 이동하여 URL 가져오기
for i,(item_code, item_name) in enumerate(zip(item_codes, item_names)):
    # 종목 페이지 이동

    try:
        URL = "https://finance.naver.com/item/coinfo.nhn?code={item_code}&target=finsum_more".format(item_code=item_code)
        finance_URL = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={item_code}&target=finsum_more".format(item_code=item_code)
        driver.get(finance_URL)

        theads = driver.find_elements_by_css_selector("thead")
        finance_columns = theads[6].text.split("\n")

        tbodys = driver.find_elements_by_css_selector('tbody')
        tbody = tbodys[12]
        finace_rows = tbody.text.split("\n")

        data.get('종목코드').append(item_code)
        data.get('종목명').append(item_name)
        data.get('dataURL').append(finance_URL)
        data.get("재무재표컬럼").append(finance_columns)
        data.get('재무재표데이터').append(finace_rows)

        time.sleep(random.randrange(1,4))

        percent = (i/len(item_codes)) * 100
        print("{:.2f}% 진행중".format(percent))
    except Exception as e:
        print("에러발생",item_code, item_name)



df = pd.DataFrame.from_dict(data)
df.to_excel("D:\\PyQt5_Sample\\Naver\\data\\URL모음.xlsx", index=False)
df.to_pickle('D:\\PyQt5_Sample\\Naver\\data\\dataPickle')
