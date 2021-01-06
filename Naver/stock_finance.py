from selenium import webdriver
import time
import pandas as pd

path = "D:\\chromedriver.exe"
driver =webdriver.Chrome(path)
item_code = "005880"
URL = "https://finance.naver.com/item/coinfo.nhn?code={item_code}&target=finsum_more".format(item_code=item_code)
driver.get(URL)

driver.switch_to.default_content()
driver.switch_to.frame('coinfo_cp')

item_cods = ['000070','000100','000220']
code = "000220"
info_URL = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd={0}&target=finsum_more".format(code)
print(info_URL)
driver.get(info_URL)



df_list = pd.read_html(info_URL, encoding='utf-8')
len(df_list)

df_list[9]


# 열 제목 추출
theads = driver.find_elements_by_css_selector("thead")
columns =theads[6].text.split("\n")

tbodys = driver.find_elements_by_css_selector('tbody')
tbody = tbodys[12]
tbody.text.split("\n")
# table = driver.find_element_by_xpath('')

driver.close()
driver.quit()