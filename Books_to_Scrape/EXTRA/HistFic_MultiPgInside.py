from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import numpy as np

driver = webdriver.Chrome()

for i in range(1,3):
    driver.get(f'https://books.toscrape.com/catalogue/category/books/historical-fiction_4/page-{i}.html')
    driver.maximize_window()
    time.sleep(2)


    for xpath_elem in driver.find_elements(By.XPATH,"//*[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']/article/h3/a"):
        links = xpath_elem.get_attribute('href')


    def chrome_headless():
        obj1 = webdriver.ChromeOptions()
        obj1.add_argument('--headless=new')
        driver = webdriver.Chrome(options=obj1)
        return driver
    
    driver1 = chrome_headless()
    driver1.get(links)
    
    UPC = [] #done 
    Product_Type = []#done 
    Price_exc  =[] #done 
    Price_inc  =[] #done 
    Tax =[] #done
    Availability =[] #done 
    reviews =[] # done
    Title = [] #done 
    Availability_num =[] 
    Star_rating =[] 
    Link_detail_page =[] # done
        
    upc = driver1.find_element(By.XPATH,"//*[@class='table table-striped']/tbody/tr[1]/td").text
    UPC.append(upc)
    # prc = driver1.find_element(By.XPATH,"//*[@class='table table-striped']/tbody/tr[2]/td").text
    # Price_exc.append(prc)
    # tx = driver1.find_element(By.XPATH,"//*[@class='table table-striped']/tbody/tr[3]/td").text
    # Tax.append(tx)
    # rv = driver1.find_element(By.XPATH,"//*[@class='table table-striped']/tbody/tr[5]/td").text
    # reviews.append(rv)
    # av_num = driver1.find_element(By.XPATH,"//*[@class='table table-striped']/tbody/tr[7]/td").text
    # Availability_num.append(av_num)

    d = {
        'UPC_NO':UPC,
        # 'Product Type' :Product_Type, 
        # 'Price(excl. tax)':Price_exc,
        # 'Price(incl. tax)':Price_inc,
        # 'Tax':Tax,
        # 'Availability':Availability,
        # 'Number of reviews':reviews
        }

df = pd.DataFrame(d)
print(df)

time.sleep(10)
driver.close()
