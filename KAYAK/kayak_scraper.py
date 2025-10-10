from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time
import openpyxl


# file-->open_workbook-->sheet-->rows-->col-->cells


# excel = openpyxl.Workbook() #make new sheet
# sheet = excel.active   
# sheet.title = 'Flight_booking' #new name change
# sheet.append(['AIRLINE_NAME','PRICE','DURATION','SOURCE','DESTINATION'])

try:
    driver = webdriver.Chrome()
    driver.get('https://www.kayak.co.in/flights/DEL-BOM/2026-01-01/2026-01-01?ucs=18sgth9&sort=bestflight_a')
    driver.maximize_window()

    # Airline_name = []
    # Price = []
    # Duration = []
    # Source  = []
    # Destination = []
        
    Airline_name = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='J0g6-operator-text']")]
    Price = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='e2GB-price-text']")]
    Duration = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='vmXl vmXl-mod-variant-large']")]
    Source = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='EFvI']/div[1]/span[1]")]
    Destination  = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='EFvI']/div[2]/span")]

    # sheet.append([Airline_name,price,Duration,Source,Destination])


    d ={

        'AIRLINE_NAME':Airline_name,
        'PRICE':Price,
        'DURATION':Duration,
        'SOURCE':Source,
        'DESTINATION':Destination

    }


    df = pd.DataFrame(d)
    print(df)
    df.to_csv('flight_tracker.csv')
    



except Exception as e:
    print(e)
# excel.save('flight_booking.xlsx')

time.sleep(10)
driver.close()

