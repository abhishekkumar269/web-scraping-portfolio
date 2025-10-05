from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import numpy as np
from datetime import date


driver = webdriver.Chrome()

try:
    all_quotes_pg = pd.DataFrame()
    for i in range(1,11):
        driver.get(f'https://quotes.toscrape.com/page/{i}/')
        driver.maximize_window()
        

        all_quotes = [quo.text for quo in driver.find_elements(By.XPATH,"//*[@class='text']")]
    
        all_Author = [auth.text for auth in driver.find_elements(By.XPATH,"//*[@class='author']")]

        all_div_tag = driver.find_elements(By.XPATH,"//div[@class='quote']")
        # print(len(all_div_tag))
        
        all_tag =[]
        for r in range(1,len(all_div_tag)+1):
            tag = []
            for i in driver.find_elements(By.XPATH,"//div["+str(r)+"][@class='quote']/div/a"):
                tag.append(i.text)
            all_tag.append(tag)
        # print(all_tag)

    # Quote | Author | Tags


        d = { 

            'Quote' : all_quotes,                                           
            'Author' :all_Author ,                  
            'Tags': all_tag                            

        }


        df = pd.DataFrame(d)                            
        all_quotes_pg  = pd.concat([df,all_quotes_pg])
        all_quotes_pg.index = np.arange(1,len(all_quotes_pg)+1)
        print(all_quotes_pg)
        # all_quotes_pg.to_csv('quotes.csv')
except Exception as e:
    print(e)

time.sleep(10)
driver.close()
