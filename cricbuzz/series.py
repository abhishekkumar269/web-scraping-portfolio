'''
| MATCH      | SERIES                | DATE                  | VENUE  | LINK         |
| ---------- | --------------------- | --------------------- | ------ | ------------ |
| IND vs SA  | India Tour of SA 2025 | Sep 15, 2025, 7:30 PM | Mumbai | https\://... |
| ENG vs AUS | The Ashes 2025        | Sep 20, 2025, 3:30 PM | London | https\://... |


'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

driver = webdriver.Chrome()
link = 'https://www.cricbuzz.com/cricket-match/live-scores/upcoming-matches'
driver.get(link)
driver.maximize_window()

all_tourment_col =  driver.find_elements(By.XPATH,"//*[@class='cb-col cb-col-100 cb-plyr-tbody cb-rank-hdr cb-lv-main']")
all_match_col = driver.find_elements(By.XPATH,"//div[@class='cb-mtch-lst cb-col cb-col-100 cb-tms-itm']")

try:


    all_match_title = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='cb-lv-scr-mtch-hdr inline-block']/a")]
    all_match_venue =[i.text for i in driver.find_elements(By.XPATH,"//*[@class='text-gray']/span[4]")]
    link = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='cb-lv-scr-mtch-hdr inline-block']/a")]
    # series_name =driver.find_element(By.XPATH,"//*[@class='cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr disp-flex cb-justify-between align-center']/a").text

    # series = [series_name] * len(all_match_title)
    # break

    d = {
                                    
        'MATCH_TITLE':all_match_title,
        # 'SERIES':series,
        'VENUE':all_match_venue,
        'LINK':link,

    }

    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    print(df)
    # df.to_csv('sport_scores.csv',index=True)

except Exception as e:
    print(e)

next = 1
for i in range(1,len(all_tourment_col)+1):
    j = driver.find_element(By.XPATH,"//*[@class='cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr disp-flex cb-justify-between align-center']/a").text
    
    print(j)



time.sleep(10)
driver.close()


