from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np 
import time
from datetime import date


all_sequential_art = pd.DataFrame()
driver = webdriver.Chrome()
try:
    for i in range(1,5):
        driver.get(f'https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-{i}.html')
        driver.maximize_window()

        Title = []
        Price = []
        Availability = []
        Product_URL = []
        Date_Scraping = []

        Title = []
        all_title = driver.find_elements(By.TAG_NAME,'h3')
        for tle in all_title:
            Title.append(tle.text)

        Price = []
        all_price = driver.find_elements(By.XPATH,"//*[@class='price_color']")
        for pc in all_price:
            Price.append(pc.text)

        Availability = []
        all_Avail = driver.find_elements(By.XPATH,"//*[@class='instock availability']")
        for al in all_Avail:
            Availability.append(al.text)


        Product_URL = []
        all_link = driver.find_elements(By.XPATH,"//*[@class='product_pod']/h3/a")
        for link in all_link:
            Product_URL.append(link.get_attribute('href'))

        
        d = {'TITLE':Title,'PRICE':Price,'AVAILABILITY':Availability,'PRODUCT_LINK':Product_URL,'DATE_SCRAPPING':date.today()}
        df = pd.DataFrame(d)
        # df.index = np.arange(1,len(df)+1)
        all_sequential_art = pd.concat([all_sequential_art,df],ignore_index=True)
        all_sequential_art.index = np.arange(1,len(all_sequential_art)+1)
        all_sequential_art.to_csv('sequential_art.csv')

        time.sleep(2)
except Exception as e:
    print(e)
driver.close()





