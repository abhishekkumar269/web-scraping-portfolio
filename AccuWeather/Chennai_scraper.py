from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

driver = webdriver.Chrome()
driver.get('https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671')
driver.maximize_window()

# City | Date | High Temp | Low Temp | Condition | Precipitation | Humidity | Wind
try:

    City = driver.find_element(By.XPATH,"//*[@class='header-city-link']/h1").text.split(',')[0]
    Date = [dt.text for dt in driver.find_elements(By.XPATH,"//*[@class='daily-list-body']/a/div/p[2]")]
    High_temp = [tem.text for tem in driver.find_elements(By.XPATH,"//*[@class='daily-list-body']/a/div[2]/div/span[1]")]
    Low_Temperature = [tem.text for tem in driver.find_elements(By.XPATH,"//*[@class='daily-list-body']/a/div[2]/div/span[2]")]
    Condition  = [con.text for con in driver.find_elements(By.XPATH,"//*[@class='daily-list-body']/a/div[3]/p")]
    Precipitation = [precp.text for precp in driver.find_elements(By.XPATH,"//*[@class='precip']")]

    cities = [City] * len(Date)


    all_links = []
    for each_xpath in driver.find_elements(By.XPATH,"//*[@class='daily-list-body']/a"):
        all_links.append(each_xpath.get_attribute('href'))

    all_wind = []
    for link in all_links:
        driver.switch_to.new_window('tab')
        driver.get(link)
        Wind = driver.find_element(By.XPATH,"//div[@class='half-day-card-content']/div[2]/div[1]/p[3]/span").text
        all_wind.append(Wind)
        # i = driver.find_element(By.XPATH,"//h3[normalize-space()='Hourly']").get_attribute('href')
        # print(i)
 
    d = {

        'City':cities,  
        'Date':Date,
        'High_Temp':High_temp,
        'Low_Tem':Low_Temperature,  
        'Condition':Condition,
        'Precipitation':Precipitation,
        'Wind':all_wind,

    }
   
    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    print(df)
    df.to_csv('chennai_weather.csv')
        
except Exception as e:
    print(e)

time.sleep(10)
driver.close()






