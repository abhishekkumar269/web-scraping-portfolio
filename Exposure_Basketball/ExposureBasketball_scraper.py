from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://basketball.exposureevents.com/youth-basketball-events')
driver.maximize_window()
time.sleep(2)

button_filter = driver.find_element(By.XPATH , "//div[@class='row']/div[1]/button[1]").click()

inital_date = '1/1/2025'
final_date = '12/31/2025'

StartDateString = driver.find_element(By.XPATH,"//*[@id='StartDateString']").clear()
driver.find_element(By.XPATH,"//*[@id='StartDateString']").send_keys(inital_date)
EndDateString = driver.find_element(By.XPATH,"//*[@id='EndDateString']").send_keys(final_date)
search_submit_button = driver.find_element(By.XPATH,"//*[@type='submit']").click()
time.sleep(5)

Data_to_extract = []
Tournament_Dates = []
Name_of_tournaments = []
Phone = []
Email = []
Director_name = []
Location_place = []
Location_state = []
    
StartDateString = driver.find_element(By.XPATH,"//*[@id='StartDateString']").get_attribute('value')

EndDateString = driver.find_element(By.XPATH,"//*[@id='EndDateString']").get_attribute('value')

for date in driver.find_elements(By.XPATH,"//span[@data-bind='html: DateFormatted']"):
    Tournament_Dates.append(date.text)

for match_name in driver.find_elements(By.XPATH,"//*[@class='text-uppercase font-weight-bold d-inline-block']"):
    Name_of_tournaments.append(match_name.text)

for location in driver.find_elements(By.XPATH,"//span[@data-bind='html: City']"):
    Location_place.append(location.text)


for state in driver.find_elements(By.XPATH,"//*[@data-bind='html: StateRegion, attr: { href: StateRegionLink }']"):
    Location_state.append(state.text)
    
d = {

    'Tournament_Dates':Tournament_Dates,
    'Name_of_tournaments':Name_of_tournaments,
    'Location_place':Location_place,
    'Location_state':Location_state

    }
    
df = pd.DataFrame(d)
df.to_csv("1JAN2025_31DEC2025.csv",index=False)
print(df)
    
time.sleep(10)
driver.close()