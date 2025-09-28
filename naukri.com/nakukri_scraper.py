from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()

for i in range(1,6):

    driver.get(f"https://www.naukri.com/")
    driver.maximize_window()

    search_field = driver.find_element(By.XPATH,"//*[@class='suggestor-input ']").send_keys('‘Python Developer’ in India')
    search_button = driver.find_element(By.XPATH,"//*[@class='qsbSubmit']").click()

    each_job_section = driver.find_elements(By.XPATH,"//*[@class='srp-jobtuple-wrapper']")

    # TITLE = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='']")]
    COMPANY = []
    LOCATION = []
    EXPERIENCE = []
    SALARY = []
    POSTED_DATE = []    
    LINK = []

time.sleep(10)
driver.close()