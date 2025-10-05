from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.adamchoi.co.uk/teamgoals/detailed')
driver.maximize_window()

driver.find_element(By.XPATH,"//*[text()='Over 2.5']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[text()='All matches']").click()
time.sleep(3)

select_country = 'Spain'

default_country = driver.find_elements(By.XPATH,"//select[@id='country']/option")


for count in default_country:
    if  'Spain' == count.text:
        count.click()
        time.sleep(2)
        break
   
all_data = driver.find_elements(By.XPATH,"//tr[@class='ng-scope isNotHighlightedRow']")

date =  []
team_1 = []
result = []
team_2 = []


for dt in driver.find_elements(By.XPATH,"//tr[@class='ng-scope isNotHighlightedRow']/td[1]"):
    date.append(dt.text)

for dt in driver.find_elements(By.XPATH,"//tr[@class='ng-scope isNotHighlightedRow']/td[3]"):
    team_1.append(dt.text)

for dt in driver.find_elements(By.XPATH,"//tr[@class='ng-scope isNotHighlightedRow']/td[4]"):
    result.append(dt.text)

for dt in driver.find_elements(By.XPATH,"//tr[@class='ng-scope isNotHighlightedRow']/td[5]"):
    team_2.append(dt.text)


d={'DATE':date,'TEAM-A':team_1,'RESULT':result,'TEAM-B':team_2}
df = pd.DataFrame(d)

# df.to_csv('La_Liga.csv')

time.sleep(10)
driver.close()