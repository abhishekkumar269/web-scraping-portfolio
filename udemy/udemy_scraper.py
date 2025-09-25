from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://www.udemy.com/courses/search/?q=python')
time.sleep(5)
driver.maximize_window()


try :

    Course_Title = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='ud-link-neutral ud-custom-focus-visible']/div")]
    Link =  [i.get_attribute('href') for i in driver.find_elements(By.XPATH,"//*[@class='ud-link-neutral ud-custom-focus-visible']")]
    Instructor =  [i.text for i in driver.find_elements(By.XPATH,"//*[@class='card-authors-module--authors--zIW0Y']/span[2]")]
    Rating = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='tag-module--tag--4CWOQ tag-module--rating--pX-4W']/span/span[2]")]
    # Students_Enrolled =  driver.find_element(By.XPATH,"//*[@class='subs-diff-module--num-learners--gXquz']/div/span").text
    # Price = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='base-price-text-module--price-part---xQlz ud-heading-md']/span[2]/span")]
    time.sleep(2)


    d = {
        'TITLE':Course_Title,
        'INSTRUCTOR':Instructor,
        'RATING':Rating,
        # 'STUDENTS':Students_Enrolled,
        # 'PRICE':Price,
        'LINK' :Link,
        }
    
    # print(d)

    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    print(df)
    df.to_csv('udemy_courses.csv',index=True)


except Exception as e:
    print(e)

time.sleep(10)
driver.close()