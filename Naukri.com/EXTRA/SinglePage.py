from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time 

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")
driver.maximize_window()

try :
    search_field = driver.find_element(By.XPATH,"//*[@class='suggestor-input ']").send_keys('‘Python Developer’ in India')
    search_button = driver.find_element(By.XPATH,"//*[@class='qsbSubmit']").click()

    # each_job_section = driver.find_elements(By.XPATH,"//*[@class='srp-jobtuple-wrapper']")
    # print(len(each_job_section))

    # for i in each_job_section:

    # TITLE = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='srp-jobtuple-wrapper']/div/div/h2")]
    # TITLE = [i.text for i in driver.find_elements(By.XPATH,"//*[@class='title ']")]
    COMPANY = [i.text for i in driver.find_elements(By.XPATH,"//a[@rel='noopener noreferrer']")]
    LOCATION = []
    EXPERIENCE = []
    SALARY = []
    POSTED_DATE = []    
    LINK = []
    print(COMPANY)

    # d = {
    #     # 'TITLE':TITLE,
    #     'COMPANY':COMPANY
    # }
    # print(COMPANY)

    # df = pd.DataFrame(d)
    # print(df)

except Exception as e:
    print(e)

time.sleep(10)
driver.close()