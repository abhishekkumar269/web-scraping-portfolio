from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver =  webdriver.Chrome()
driver.get('https://www.reddit.com/search/?q=r%2Felectricvehicles&cId=ecab0181-4350-4f7e-ab3a-3cbd7dc7414b&iId=65068219-76dc-4410-b6a8-96d2bf1d7b9a')
driver.maximize_window()

try:

    post_title = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='w-full flex flex-col items-start min-w-0 ']/a")]
    vote =[i.text for i in driver.find_elements(By.XPATH,"//*[@class='w-full flex flex-col items-start min-w-0 ']/div[2]/span[1]")]
    date = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='w-full flex flex-col items-start min-w-0 ']/div/div/span/faceplate-timeago")]
    post_link = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='w-full flex flex-col items-start min-w-0 ']/a")]
    comment = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='w-full flex flex-col items-start min-w-0 ']/div[2]/span[3]")]


    d = {

        'POST_TITLE':post_title,
        'POST_LINK':post_link,
        'POST_DATE':date,
        'POST_UPVOTE':vote,
        'comment':comment
    }



    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    # print(df)
    df.to_csv('reddit_car.csv',index=True)


except Exception as e:
    print(e)

time.sleep(10)
driver.close()