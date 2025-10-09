from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.udemy.com/courses/search/?q=python')
driver.implicitly_wait(5)
driver.maximize_window()

def headless_chrome ():
    obj1 =webdriver.ChromeOptions()
    obj1.add_argument('--headless=new')
    driver = webdriver.Chrome(options=obj1)
    return driver

driver1 = headless_chrome()


try :
    Course_Title = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ud-link-neutral ud-custom-focus-visible']")]
    Link =  driver.find_element(By.XPATH,"//*[@class='ud-link-neutral ud-custom-focus-visible']")
    k =Link.get_attribute('href')

    driver1.get(k)
        # print()

    Instructor =  driver1.find_element(By.XPATH,"//*[@class='ud-btn ud-btn-medium ud-btn-link ud-heading-sm ud-text-sm ud-instructor-links']/span").text
    # Rating = driver1.find_element(By.XPATH,"//*[@class='ud-heading-xl']").text
    # Students_Enrolled =  driver1.find_element(By.XPATH,"//*[@class='subs-diff-module--num-learners--gXquz']/div/span").text
    # Price = driver.find_element(By.XPATH,"//div[@id='u1270-tabs--211-content-0']//div//div[@class='generic-purchase-section--main-cta-container--LGsJD']//div[@class='generic-purchase-section--buy-box-main--W9rN0']//div[@class='buy-box--buy-box--KeMlj']//div[@class='buy-box--buy-box-item--wT5bJ']//div//div[@class='base-price-text-module--container--Sfv-5 ud-clp-price-text']//div[@class='base-price-text-module--price-part---xQlz ud-clp-discount-price ud-heading-xl']//span//span[contains(text(),'₹549')]").text

    d = {
        # 'TITLE':Course_Title,
        'INSTRUCTOR':Instructor,
        # ' RATING':Rating,
        # 'STUDENTS':Students_Enrolled,
        # 'PRICE':Price,
        # 'LINK' :Link,
        }
    print(d)

    # df = pd.DataFrame(d)
    # print(df)
except Exception as e:
    print(e)


time.sleep(10)
driver.close()