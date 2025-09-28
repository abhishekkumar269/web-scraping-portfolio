'''# Open page:
# https://tracreports.org/phptools/immigration/ntanew/

# Extract fields (from table):

# Date / Period

# Location (court name)

# Case Count / Filings

# Other numeric fields (jo bhi columns visible hain).

# Save output as:
# trac_immigration_cases.csv

# Nationality | County | Fiscal Year | Case Group | Number of Cases | How Long in U.S.
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get('https://tracreports.org/phptools/immigration/ntanew/')
driver.maximize_window()

try:
    time.sleep(5)  
    all_cases_button = driver.find_element(By.XPATH,"//*[@id='controls_group1']/div/div[2]/input").click()
    Fiscal_Year_button = driver.find_element(By.XPATH,"//*[@id='controls_group2']/div[1]/div[3]/label").click()

    #nation select
    picker1_click = driver.find_element(By.XPATH,"//*[@id='headlessui-listbox-button-1']").click()
    picker1_elements = [i for i in driver.find_elements(By.XPATH,"//*[@aria-labelledby='headlessui-listbox-button-1']/li/li")]
    # all_country =[i for i in driver.find_elements(By.XPATH,"//*[@class='flex flex-col basis-1/3']/div[2]/div/div/div/table/tbody/tr")] 
    all_count = [i for i in driver.find_elements(By.XPATH,"//*[@class='shadow border-b border-gray-200 sm:rounded-lg']/table/tbody/tr")]
    print(all_count)
    
    my_select = 'Nationality'
    for elem in picker1_elements:
        if my_select == elem.text:
            elem.click()
            break

    # my_requ_country = 'China'      
    # for country in all_country:
    #     print(country.text)
        # if my_requ_country == country.text:
        #     country.click()
        #     break

    # gender_picker = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='flex flex-row md:w-full']/div[2]")]
    # represented_picker = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='flex flex-row md:w-full']/div[3]")]

except Exception as e:
    print(e)

time.sleep(10)
driver.close()