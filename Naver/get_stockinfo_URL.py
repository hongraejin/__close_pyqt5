import pandas as pd
from selenium import webdriver

path = "D:\\chromedriver.exe"

driver = webdriver.Chrome(path)

item_df = pd.read_csv("D:\\PyQt5_Sample\\Naver\\종목.csv")
print(item_df)

# 모든 종목코드를 읽는다.
# 정보가 들어있는 URL 을 가져온다.




item_code = "005880"
URL = "https://finance.naver.com/item/coinfo.nhn?code={item_code}&target=finsum_more".format(item_code=item_code)
driver.get(URL)
frame = driver.find_element_by_id("coinfo_cp")
frame.get_attribute('src')