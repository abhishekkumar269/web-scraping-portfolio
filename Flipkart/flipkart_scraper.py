from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

try:

    all_data = pd.DataFrame()

    for i in range(1,4):
        driver.get('https://www.flipkart.com/search?q=laptops+under+50000&page={}'.format(i))
        driver.maximize_window()

        model_name = []
        all_lap_names = driver.find_elements(By.XPATH,"//*[@class='KzDlHZ']")
        for lap_name in all_lap_names:
            model_name.append(lap_name.text)

        price =[]
        all_prices = driver.find_elements(By.XPATH,"//*[@class='Nx9bqj _4b5DiR']")
        for pr in all_prices:
            price.append(pr.text)

        rating = []
        all_ratings = driver.find_elements(By.XPATH,"//*[@class='Y1HWO0']/div")
        for rat in all_ratings:
            rating.append(rat.text)

        number_of_reviews = []
        all_reviews = driver.find_elements(By.XPATH,"//span[@class='Wphh3N']/span/span[1]")
        for rev in all_reviews:
            number_of_reviews.append(rev.text)

        d = {'MODEL_NAME':model_name,'PRICE':price,'RATING':rating,'REVIEW':number_of_reviews}
        
        df = pd.DataFrame(d)

        all_data = pd.concat([all_data,df],ignore_index =True)

        all_data.to_csv('mob.csv')
        # print(all_data)
        time.sleep(3)
        
                 
except Exception as e:
    print(e)

time.sleep(10)
driver.close()