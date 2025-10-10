from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver=webdriver.Chrome()
driver.get('https://singaporecruise.com.sg/schedule/ferries/?ferry-status=departure&date=&time=all&terminal=all&port=all&ferry=all')
driver.maximize_window()

all_dates = driver.find_elements(By.XPATH,"//*[@data-label='DATE']")
all_time = driver.find_elements(By.XPATH,"//*[@data-label='TIME']")
all_status = driver.find_elements(By.XPATH,"//*[@data-label='STATUS']")


departure_date = []
for date in all_dates:
    departure_date.append(date.text)

departure_time = []
for tme in  all_time:
    departure_time.append(tme.text)

status = []
for st in all_status:
    status.append(st.text)

d = {'DATE':departure_date,'TIME':departure_time,'STATUS':status}
df= pd.DataFrame(d)
print(df)
df.to_csv("ferri_departure.csv")

time.sleep(5)
driver.close()

