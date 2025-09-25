'''
| TITLE               | PRICE   | LOCATION      | DETAILS                       | LINK         |
| ------------------- | ------- | ------------- | ----------------------------- | ------------ |
| 2 BHK Apartment     | ₹45 L   | Dwarka, Delhi | 900 sqft, Ready to Move       | https\://... |
| 3 BHK Builder Floor | ₹1.2 Cr | Rohini, Delhi | 1500 sqft, Under Construction | https\://... |
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.magicbricks.com/property-for-sale-rent-in-Delhi-NCR/residential-real-estate-Delhi-NCR')
driver.maximize_window()

search_button = driver.find_element(By.XPATH,"//*[@class='mb-search__btn']").click()

try :

    # Link = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='mb-srp__list']")]
    Title = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='mb-srp__card--title']")]
    Price  = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='mb-srp__card__price']/div[1]")]
    # Location = []
    # Property_Type = []
    # Link = []

    d = {
        
        'TITLE':Title,
        'PRICE':Price,
        }
    
    print(d)

    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    df.to_csv('magicbricks_data.csv',index=True)

except Exception as e:
    print(e)

time.sleep(10)
driver.close()