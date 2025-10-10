from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
from datetime import date,time
import time

driver=webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue')

# Rank /done# Name /done# Industry /done# Revenue (USD millions) /done# Headquarters# Employees /done #Country/don

try:

    Name= [data.text for data in driver.find_elements(By.XPATH,"//*[@class='wikitable sortable sticky-header-multi sort-under jquery-tablesorter']/tbody/tr/td[1]")]
    Industry = [data.text for data in driver.find_elements(By.XPATH,"//*[@class='wikitable sortable sticky-header-multi sort-under jquery-tablesorter']/tbody/tr/td[2]")]
    Revenue = [data.text for data in driver.find_elements(By.XPATH,"//*[@class='wikitable sortable sticky-header-multi sort-under jquery-tablesorter']/tbody/tr/td[3]")]
    Employees = [data.text for data in driver.find_elements(By.XPATH,"//*[@class='wikitable sortable sticky-header-multi sort-under jquery-tablesorter']/tbody/tr/td[5]")]
    country = [data.text for data in driver.find_elements(By.XPATH,"//*[@class='wikitable sortable sticky-header-multi sort-under jquery-tablesorter']/tbody/tr/td[6]")]

    comp_link = [data.get_attribute('href') for data in driver.find_elements(By.XPATH,"//*[@class='wikitable sortable sticky-header-multi sort-under jquery-tablesorter']/tbody/tr/td[1]/a")]
    all_location = []

    def headless_chrome():
        ops = webdriver.ChromeOptions()
        ops.add_argument("--headless=new")
        driver = webdriver.Chrome(options=ops)
        return driver 
                
    driver1 = headless_chrome()

    for link in comp_link:  
        driver1.get(link)
        tb = driver1.find_elements(By.XPATH,"//*[@class='infobox ib-company vcard']/tbody")
        all_tb_header = driver1.find_elements(By.XPATH,"//*[@class='infobox ib-company vcard']/tbody/tr/th")
        all_tb_data = driver1.find_elements(By.XPATH,"//*[@class='infobox ib-company vcard']/tbody/tr/td")

        Headquarters = 'Headquarters'
        for i in range(3,len(all_tb_header)+1):
            try:
                all_title=driver1.find_element(By.XPATH,"//*[@class='infobox ib-company vcard']/tbody/tr["+str(i)+"]/th").text

                if  all_title == Headquarters:
                    all_location.append(driver1.find_element(By.XPATH,"//*[@class='infobox ib-company vcard']/tbody/tr["+str(i)+"]/td").text)
            except Exception :
                continue

            
    d = {


    'Name':Name,
    'Industry':Industry,
    'Revenue' :Revenue,
    'Headquarters':all_location,
    'Employees':Employees,
    'Country':country,


    }

    df = pd.DataFrame(d)
    df.index = np.arange(1,len(df)+1)
    df.index.name = 'Rank'
    print(df)
    df.to_csv('fortune500.csv',index_label='Rank')
except Exception as e:
    print(e)

time.sleep(10)
driver.close



