'''
| TITLE                                           | LINK         | TIME                 |
| ----------------------------------------------- | ------------ | -------------------- |
| Sensex rises 500 points as banking stocks rally | https\://... | Sep 13, 2025, 2:30PM |
| Rupee weakens against dollar amid global cues   | https\://... | Sep 13, 2025, 1:45PM |
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time
import openpyxl

# file-->open_workbook-->sheet-->rows-->col-->cells
# excel = openpyxl.Workbook() #make new sheet
# sheet = excel.active   
# sheet.title = 'Flight_booking' #new name change
# sheet.append(['TITLE',' LINK','TIME'])

try:

    driver  = webdriver.Chrome()
    driver.get('https://www.business-standard.com/markets')
    driver.maximize_window()

    time.sleep(3)
    driver.find_element(By.XPATH,"//body/div[@id='__next']/div[@class='Nws_hp_top_rowpannel wrapper section-flex']/div[@class='Nws_hp_70 flex-70']/div[2]/div[2]/div[2]/div[2]/a[1]").click()

    title = [i.text for i in driver.find_elements(By.XPATH,"//a[@class='smallcard-title']")]
    link = [i.get_attribute('href')for i in driver.find_elements(By.XPATH,"//*[@class='smallcard-title']")]
    tim = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='listingstyle_updtText__lnZb7']/span")]
    # sheet.append([title,link,tim])
    
    d = {

        'TITLE':title,
        ' LINK':link,
        'TIME':tim
    }

    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    print(df)
    df.to_csv('finance_news_bs.csv')

except Exception as e:
    print(e)    
# excel.save('finance_news_bs.xlsx')

time.sleep(10)
driver.close()

