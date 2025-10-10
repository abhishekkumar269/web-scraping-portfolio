from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get('https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671')


date = []
for dt in driver.find_elements(By.XPATH,"//*[@class='daily-list-body']/a/div/p[2]"):
    date.append(dt.text)

Condition  = [con.text for con in driver.find_elements(By.XPATH,"//*[@class='daily-list-body']/a/div[3]/p")]

High_temp = [tem.text for tem in driver.find_elements(By.XPATH,"//*[@class='daily-list-body']/div[2]/a/div/span[1]")]
Low_Temperature = [tem.text for tem in driver.find_elements(By.XPATH,"//*[@class='daily-list-body']/a/div[2]/div/span[2]")]
Precipitation = [prep.text for prep in driver.find_elements(By.XPATH,"//*[@class='daily-list-body']/a/div[4]/svg")]
Humidity = driver.find_element(By.XPATH,"//*[@class='spaced-content detail']span[2]").text
Wind = driver.find_element(By.XPATH,"//*[@class='spaced-content detail']span[2]").text

d = {

    # 'City':,
    'Date':date,
    # 'High_Temp':,
    # 'Low_Tem':,
    'Condition':Condition,
    'Precipitation':Precipitation,
    # 'Humidity':,
    # 'Wind':,

}

dt = pd.DataFrame(d)
print(dt)

time.sleep(5)
driver.close()