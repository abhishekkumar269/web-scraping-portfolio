from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException
import time
import pandas as pd


driver=webdriver.Chrome()
mywait = WebDriverWait(driver,10)

driver.get('https://singaporecruise.com.sg/schedule/ferries/')
driver.maximize_window()


time.sleep(5)
date_picker_obj1 = driver.find_element(By.XPATH,"//*[@class='banner-schedule__searchform-icon calender-icon']")
date_picker_obj1.click()

# all_active_date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

try:
    for i in driver.find_elements(By.XPATH,"//*[@class='ui-datepicker-calendar']/tbody/tr/td/a") :

        j = driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr[6]//td[1]//a")
        # print(j.text)
    
    mywait.until(EC.presence_of_all_elements_located(j))
    j.click()
except Exception as e:
    print(e)



# # captur_date = driver.find_element(By.XPATH,"//input[@name='date']").get_attribute('value')
# # print(captur_date)

# curr_date = driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr[3]//td[5]//a").text
# # print(capt_curr_date)
# end_date = driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr[6]//td[1]//a").text

# conv_capt_curr_dat = int(curr_date)
# # print(conv_capt_curr_dat)
# conv_end_date = int(end_date)
# # print(conv_end_date)    

# all_active_date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
# try:
#     for i in all_active_date:
#         if conv_capt_curr_dat == conv_end_date:
#             break

#         else:
#             # date_picker = driver.find_element(By.XPATH,"//*[@class='banner-schedule__searchform-icon calender-icon']").click()
#             i.click()
    


# except Exception as e:
#     print(e)


time.sleep(10)
driver.close()