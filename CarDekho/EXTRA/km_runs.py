from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

try:

    driver = webdriver.Chrome()
    driver.get('https://www.cardekho.com/used-cars+in+new-delhi')
    driver.maximize_window()

    Car_Name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='title']/a")]
    Price  = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='bottom_container']/div[2]/p")]
    Location = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='distanceText']")]
    # KM_Run = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='dotsDetails']")]
    Link = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='title']/a")]



    d ={

        'CAR_NAME':Car_Name,
        'PRICE':Price,
        'LOCATION':Location,
        # 'KM_RUN':KM_Run,
        'LINK':Link

    }

    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    df.to_csv('cars_data.csv' ,index= True)

except Exception as e:
    print(e)

time.sleep(10)
driver.close()
