from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

driver = webdriver.Chrome()

all_data = pd.DataFrame()
for i in range(1,2):
    driver.get(f'https://www.screener.in/market/IN02/?limit=50&page={i}')
    driver.maximize_window()

    # def headless_chrome():
    #     obj1 = webdriver.ChromeOptions()
    #     obj1.add_argument('--headless=new')
    #     driver = webdriver.Chrome(options=obj1)
    #     return driver

    # driver1 = headless_chrome()

    company_name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='data-table text-nowrap striped mark-visited no-scroll-right']/tbody/tr/td[2]/a")]
    company_link = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='data-table text-nowrap striped mark-visited no-scroll-right']/tbody/tr/td[2]/a")]

    d = {

        'COMPANY_NAME':company_name,
        'COMPANY_LINK':company_link

    }

    df = pd.DataFrame(d)

    all_data = pd.concat([df,all_data],ignore_index=True)
    all_data.index = np.arange(1,len(all_data)+1)

    all_data.to_csv('company_list.csv')
    print(all_data)
    time.sleep(1)

time.sleep(10)
driver.close()