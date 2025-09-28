from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get('https://www.accuweather.com/en/in/mumbai/204842/weather-forecast/204842')

city1 =  'Bengaluru'
city2 =  'Mumbai'
city3 = 'Chennai'
links = []

links.append(driver.find_element(By.XPATH,"//*[@class='nearby-locations-list']/a[5]").get_attribute('href'))
links.append(driver.find_element(By.XPATH,"//*[@class='nearby-locations-list']/a[8]").get_attribute('href'))
links.append(driver.find_element(By.XPATH,"//*[@class='nearby-locations-list']/a[15]").get_attribute('href'))


driver.switch_to.new_window('tab')
driver.get(links[0])
# driver.switch_to.new_window('tab')
# driver.get(links[1])
# driver.switch_to.new_window('tab')
# driver.get(links[2])

date = []
for dt in driver.find_elements(By.XPATH,"//*[@class='daily-list-item']/div/p[2]"):
    date.append(dt.text)
    print(date)
Condition  = [con.text for con in driver.find_elements(By.XPATH,"//*[@class='daily-list-item ']/div[3]/p")]
# High_temp = 
# Low_Temperature = 
# Precipitation = 
# Humidity = 
# Wind = 

# d = {

#     # 'City':,
#     'Date':date,
#     # 'High_Temp':,
#     # 'Low_Tem':,
#     'Condition':Condition,
#     # 'Precipitation':,
#     # 'Humidity':,
#     # 'Wind':,

# }

# dt = pd.DataFrame(d)
# print(dt)




time.sleep(5)
driver.close()