from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

driver = webdriver.Chrome()
link = 'https://www.imdb.com/chart/top/'
driver.get(link)
driver.maximize_window()

try:

    all_movie_name = [i.text.split('.')[1] for i in driver.find_elements(By.XPATH,"//*[@class='ipc-metadata-list-summary-item']//div//div//div//div/div[2]/div[1]/a/h3")]
    all_movie_rating = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ipc-metadata-list-summary-item']//div//div//div//div/div[2]/span/div/span/span[1]")]
    all_movie_peoplevote = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ipc-metadata-list-summary-item']//div//div//div//div/div[2]/span/div/span/span[2]")]
    all_movie_year = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ipc-metadata-list-summary-item']//div//div//div//div//div[2]//div[2]//span[1]")]

    d = {

        'MOVIE_NAME':all_movie_name,   
        'RATING': all_movie_rating  ,
        'NO_OF_PEOPLEVOTING':all_movie_peoplevote,
        'YEAR_OF_RELASE': all_movie_year,                   

    }

    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    print(df)
    df.to_csv('Imbd_Top_250.csv')

except Exception as e:
    print(e)

time.sleep(10)
driver.close()
