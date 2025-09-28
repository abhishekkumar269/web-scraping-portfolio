from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time 

driver = webdriver.Chrome()
driver.get('https://www.coursera.org/search?query=python&index=prod_all_launched_products_term_optimizatio')
driver.maximize_window()


CourseTitle = []
Instructor_University = []
Rating = []
Enrolled_Students =[]
Course_Link = []







time.sleep(10)
driver.close()