from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time 

driver = webdriver.Chrome()
driver.get('https://www.magicbricks.com/property-for-sale-rent-in-Delhi-NCR/residential-real-estate-Delhi-NCR')
driver.maximize_window()

def headless_chrome():
    obj1 = webdriver.ChromeOptions()
    obj1.add_argument('--headless=new')
    driver = webdriver.Chrome(options=obj1)
    return driver
    
driver1 = headless_chrome()

search_button = driver.find_element(By.XPATH,"//*[@class='mb-search__btn']").click()

Title  = []
Price  = []
Location = []
Size = []
Bedrooms_Bathrooms = []
Property_Type = []
Posted_Agent_Owner_Builder = []

all_flats_link = [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='mb-srp__list']")]
Title = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='mb-srp__card--title']")]


d = {
    'TITLE':Title,
    # 'PRICE':Price,
    'LOCATION':Location,
    'SIZE':Size,

    }

df = pd.DataFrame(d)
print(df)

time.sleep(10)
driver.close()