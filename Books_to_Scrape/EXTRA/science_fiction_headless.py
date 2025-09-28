from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver =  webdriver.Chrome()
driver.get('https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html')
driver.maximize_window()

links = []
all_books_xpath = driver.find_elements(By.XPATH,"//*[@class='product_pod']/h3/a") #16
for i in all_books_xpath:
    links.append(i.get_attribute('href'))

def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    driver  = webdriver.Chrome(options=ops)
    return driver


driver1 = headless_chrome()

all_title = []
all_price = []
all_Stock_number = []
all_Product_description = []
all_UPC = []
all_Category = []

for link in links:
    driver1.get(link) # print((driver.current_url))

    title = driver1.find_element(By.XPATH,"//*[@class='col-sm-6 product_main']/h1").text
    all_title.append(title)

    Price = driver1.find_element(By.XPATH,"//div[@class='col-sm-6 product_main']/p[1]").text
    all_price.append(Price)

    Stock_number = driver1.find_element(By.XPATH,"//*[@class='table table-striped']/tbody/tr[6]/td").text
    all_Stock_number.append(Stock_number)

    Product_description=driver1.find_element(By.XPATH,"//*[@class='product_page']/p").text
    all_Product_description.append(Product_description)

    UPC=driver1.find_element(By.XPATH,"//*[@class='table table-striped']/tbody/tr[1]/td").text
    all_UPC.append(UPC)

    Category = driver1.find_element(By.XPATH,"//*[@class='breadcrumb']/li[3]").text
    all_Category.append(Category)


    d = {

        'TITLE':all_title,
        'PRICE':all_price,
        'STOCKS':all_Stock_number,
        'PRODUCT_DESC':all_Product_description,
        'URC':all_UPC,
        'CATEGORY':all_Category

    }

# print(d) 


df = pd.DataFrame(d)
# print(df)

df.to_csv('science_fiction_upc.csv',index=True)



time.sleep(10)
driver.close()













    

