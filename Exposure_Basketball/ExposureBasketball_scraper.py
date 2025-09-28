from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://basketball.exposureevents.com/youth-basketball-events')
driver.maximize_window()
time.sleep(2)

# each_section = driver.find_elements(By.XPATH,"//*[@class='col-12 mb-3']")

try:

    button_filter = driver.find_element(By.XPATH , "//div[@class='row']/div[1]/button[1]").click()

    inital_date = '1/1/2025'
    final_date = '12/31/2025'

    StartDateString = driver.find_element(By.XPATH,"//*[@id='StartDateString']").clear()
    driver.find_element(By.XPATH,"//*[@id='StartDateString']").send_keys(inital_date)
    EndDateString = driver.find_element(By.XPATH,"//*[@id='EndDateString']").send_keys(final_date)
    search_submit_button = driver.find_element(By.XPATH,"//*[@type='submit']").click()
    time.sleep(5)

    start_page = driver.find_element(By.XPATH,"//ul[@class='pagination justify-content-center justify-content-md-end mb-0']/li[3]/a").text
    desired_target = driver.find_element(By.XPATH,"//ul[@class='pagination justify-content-center justify-content-md-end mb-0']/li[6]/a").text
    
    conv_int_start = int(start_page)
    conv_int_target = int(desired_target)
    
    all_data = []

    for i in range(conv_int_start,conv_int_target+1):
        driver.find_element(By.XPATH,"//*[@data-bind='click: nextPage']/i").click()
        time.sleep(5)
                   
except Exception as e:
    print(e)
    
time.sleep(10)
driver.close()