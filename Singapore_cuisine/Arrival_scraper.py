from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver=webdriver.Chrome()
driver.get('https://singaporecruise.com.sg/schedule/ferries/')
driver.maximize_window()

all_dates = driver.find_elements(By.XPATH,"//*[@data-label='DATE']")
all_time = driver.find_elements(By.XPATH,"//*[@data-label='TIME']")
all_status = driver.find_elements(By.XPATH,"//*[@data-label='STATUS']")



arrival_date = []
for date in all_dates:
    arrival_date.append(date.text)

arrival_time = []
for tme in  all_time:
    arrival_time.append(tme.text)

status = []
for st in all_status:
    status.append(st.text)

d = {'DATE':arrival_date,'TIME':arrival_time ,'STATUS':status}
df= pd.DataFrame(d)
print(df)

time.sleep(10)
driver.close()

