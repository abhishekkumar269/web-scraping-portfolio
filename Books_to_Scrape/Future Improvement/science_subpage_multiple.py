from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date
import pandas as pd
import numpy as np

driver = webdriver.Chrome()
parent =driver.get('https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html')
driver.maximize_window()

all_books_xpath = driver.find_elements(By.XPATH,"//*[@class='product_pod']/h3/a")
all_books_link = []

for i in all_books_xpath:
    all_books_link.append(i.get_attribute('href'))

#opening link in differnt tab
for i in all_books_link:
    driver.switch_to.new_window()
    driver.get(i)

#capture for all reuired data
    title = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='col-sm-6 product_main']/h1")]
    Price = [i.text for i in driver.find_elements(By.XPATH,"//div[@class='col-sm-6 product_main']/p[1]")]
    Stock_number = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='table table-striped']/tbody/tr[6]/td")]
    Product_description=[i.text for  i in driver.find_elements(By.XPATH,"//*[@class='product_page']/p")]
    UPC=[i.text for i in driver.find_elements(By.XPATH,"//*[@class='table table-striped']/tbody/tr[1]/td")]
    Category = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='breadcrumb']/li[3]")]

    d = {
        'TITLE':title,
        'PRICE':Price,
        'STOCKS':Stock_number,
        'PRODUCT_DESC':Product_description,
        'URC':UPC,
        'CATEGORY':Category
    }

    # print(d)
    df = pd.DataFrame(d)
    print(df)
    # df.to_csv('science_books.csv')


time.sleep(10)
driver.close()


























