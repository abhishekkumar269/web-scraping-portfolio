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

try:


    all_match_title = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='cb-lv-scr-mtch-hdr inline-block']/a")]
    all_match_venue =[i.text for i in driver.find_elements(By.XPATH,"//*[@class='text-gray']/span[4]")]
    link = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='cb-lv-scr-mtch-hdr inline-block']/a")]
    date = [i.text for i in driver.find_elements(By.XPATH,"//div[@class='cb-mtch-lst cb-col cb-col-100 cb-tms-itm']/div[1]/div/div/span")]


    d = {
                                    
        'MATCH_TITLE':all_match_title,
        'VENUE':all_match_venue,
        'LINK':link,

    }

    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    print(df)
    df.to_csv('sport_scores.csv',index=True)

except Exception as e:
    print(e)

time.sleep(10)
driver.close()


