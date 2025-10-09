from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.reddit.com/search/?q=r%2Felectricvehicles&cId=ecab0181-4350-4f7e-ab3a-3cbd7dc7414b&iId=65068219-76dc-4410-b6a8-96d2bf1d7b9a')
driver.maximize_window()

try:



    post_title = driver.find_element(By.XPATH,"//*[@class='w-full flex flex-col items-start min-w-0 ']/a").text
    vote =driver.find_element(By.XPATH,"//*[@class='w-full flex flex-col items-start min-w-0 ']/div[2]/span").text
    date = driver.find_element(By.XPATH,"//*[@class='w-full flex flex-col items-start min-w-0 ']/div/div/span/faceplate-timeago").text
    post_link = driver.find_element(By.XPATH,"//*[@class='w-full flex flex-col items-start min-w-0 ']/a").get_attribute('href')
    comment = driver.find_element(By.XPATH,"//*[@class='w-full flex flex-col items-start min-w-0 ']/div[2]/span[3]").text


    d = {

        'POST':[post_title],
        'POST_LINK':[post_link],
        'POST_DATE':[date],
        'Vote':[vote],
        'comment':[comment]
    }



    df = pd.DataFrame(d)
    print(df)

except Exception as e:
    print(e)

time.sleep(10)
driver.close()