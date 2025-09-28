from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date
import pandas as pd
import numpy as np

driver = webdriver.Chrome()
driver.get('https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html')
driver.maximize_window()

'''
Title
Price
Availability / Stock number
Product description
UPC
Category
'''

driver.find_element(By.XPATH,"//*[@class='product_pod']/h3/a").click()

try:
    
    title = driver.find_element(By.XPATH,"//*[@class='col-sm-6 product_main']/h1").text

    Price = driver.find_element(By.XPATH,"//div[@class='col-sm-6 product_main']/p[1]").text

    Stock_number = driver.find_element(By.XPATH,"//*[@class='table table-striped']/tbody/tr[6]/td").text

    Product_description=driver.find_element(By.XPATH,"//*[@class='product_page']/p").text

    UPC=driver.find_element(By.XPATH,"//*[@class='table table-striped']/tbody/tr[1]/td").text

    Category = driver.find_element(By.XPATH,"//*[@class='breadcrumb']/li[3]").text

    d = {

        'TITLE':[title],
        'PRICE':[Price],
        'STOCKS':[Stock_number],
        'PRODUCT_DESC':[Product_description],
        'URC':[UPC],
        'CATEGORY':[Category]

    }

    df = pd.DataFrame(d)

    df.to_csv('science_books.csv')
    time.sleep(3)
    driver.back()
    
except Exception as e:
    print(e)

time.sleep(10)
driver.close()







