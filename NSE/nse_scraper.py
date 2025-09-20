from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.nseindia.com/market-data/live-equity-market')
driver.maximize_window()
time.sleep(10)

Company_name = []
Last_traded_price  = []
Change = []

Company_name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class=' ']/td[1]")]
Last_traded_price  = [i.text for i in driver.find_elements(By.XPATH,"//*[@class=' ']/td[6]")]
Change = [i.text for i in driver.find_elements(By.XPATH,"//*[@class=' ']/td[9]")]

d = {
    'COMPANY':Company_name,
    'LTP':Last_traded_price,
    'CHANGE':Change
    }

df = pd.DataFrame(d)
df.index = np.arange(1,len(df)+1)
print(df)
# df.to_csv('company_details.csv',index=True)

time.sleep(10)
driver.close()