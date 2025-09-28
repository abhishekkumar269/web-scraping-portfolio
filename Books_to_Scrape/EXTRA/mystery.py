from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date
import pandas as pd

driver = webdriver.Chrome()

all_mystery_books = pd.DataFrame()
for i in range(1,3):

    driver.get(f'https://books.toscrape.com/catalogue/category/books/mystery_3/page-{i}.html')
    driver.maximize_window()

    Title = []
    all_books_name = driver.find_elements(By.TAG_NAME,'h3')
    for book in all_books_name:
        Title.append(book.text)

    Price = []
    all_price = driver.find_elements(By.XPATH,"//*[@class='product_price']/p[1]")
    for price in all_price:
        Price.append(price.text)

    Availability = []
    avalibity = driver.find_elements(By.XPATH,"//*[@class='instock availability']")
    for aval in avalibity:
        Availability.append(aval.text)

    Product_URL = []
    product_link = driver.find_elements(By.XPATH,"//*[@class='product_pod']/h3/a")
    for link in product_link:
        Product_URL.append(link.get_attribute('href'))


    d = {'TITLE':Title,
     'PRICE':Price,
     'AVALIBITY':Availability,
     'PRODUCT_URL':Product_URL,
     'DATE_SCRAPPING':date.today()
     }
    
    df = pd.DataFrame(d)

    all_mystery_books = pd.concat([all_mystery_books,df],ignore_index=True)
    
    all_mystery_books.to_csv('books_day3.csv')

    time.sleep(3)


time.sleep(10)
driver.close()