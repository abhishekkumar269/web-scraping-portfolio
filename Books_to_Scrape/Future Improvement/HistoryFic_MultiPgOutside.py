from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import numpy as np

driver = webdriver.Chrome()


all_data = pd.DataFrame()
for i in range(1,3):

    driver.get(f'https://books.toscrape.com/catalogue/category/books/historical-fiction_4/page-{i}.html')
    driver.maximize_window()

    UPC = [] 
    Product_Type = []
    Price_exc  =[] #done 
    Price_inc  =[] 
    Tax =[] 
    Availability =[] #done 
    reviews =[] 
    Title = [] #done 
    Availability_num =[] 
    Star_rating =[] 
    Link_detail_page =[] # done

    '''
    # for elem in driver.find_element(By.XPATH,"//*[@class='table table-striped']/tbody/tr[1]/td")
        # UPC.append(elem1.text)

    # for elem in driver.find_elements(By.XPATH,"//*[@class='table table-striped']/tbody/tr[2]/td"):
    #     print(len(elem))
    #     # Product_Type.append(elem.text)

    # for elem in driver.find_elements(By.XPATH,"//*[@class='table table-striped']/tbody/tr[3]/td"):
    #     Price_exc.append(elem.text)

    # for elem in driver.find_elements(By.XPATH,"//*[@class='table table-striped']/tbody/tr[4]/td"):
    #     Price_inc.append(elem.text)

    # for elem in driver.find_elements(By.XPATH,"//*[@class='table table-striped']/tbody/tr[5]/td"):
    #     Tax.append(elem.text)

    # for elem in driver.find_elements(By.XPATH,"//*[@class='table table-striped']/tbody/tr[6]/td"):
    #     Availability.append(elem.text)

    # for elem in driver.find_elements(By.XPATH,"//*[@class='table table-striped']/tbody/tr[7]/td"):
    #     reviews.append(elem.text)

    # for elem in driver.find_elements(By.XPATH,"//*[@class='col-sm-6 product_main']/h1"):
    #     Title.append(elem.text)

    # for elem in driver.find_elements(By.XPATH,"//*[@class='table table-striped']/tbody/tr[1]/td"):
    #     elem.text

    # for elem in driver.find_elements(By.XPATH,"//*[@class='table table-striped']/tbody/tr[1]/td"):
    #     elem.text

    # d = {
    #     'UPC_NO':UPC,
    #     'Product Type' :Product_Type, 
    #     'Price(excl. tax)':Price_exc,
    #     'Price(incl. tax)':Price_inc,
    #     'Tax':Tax,
    #     'Availability':Availability,
    #     'Number of reviews':reviews
    #     }

    # df = pd.DataFrame(d)
    # print(df)

    '''

    for elem in driver.find_elements(By.XPATH,"//*[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']/article/h3/a"):
        Title.append(elem.text)

    for elem in driver.find_elements(By.XPATH,"//*[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']/article/div/p[1]"):
        Price_exc.append(elem.text)

    for elem in driver.find_elements(By.XPATH,"//*[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']/article/div/p[2]"):
        Availability.append(elem.text)

    for elem in driver.find_elements(By.XPATH,"//*[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']/article/h3/a"):
        Link_detail_page.append(elem.get_attribute('href'))


    d = {

        # 'UPC_NO':UPC,
        # 'Product Type' :Product_Type, 
        
        # 'Price(incl. tax)':Price_inc,
        # 'Tax':Tax,
                
        'Title':Title,
        'product_link':Link_detail_page,
        'Price(excl. tax)':Price_exc,
        'Availability':Availability,

    }
    df = pd.DataFrame(d)

    df.index = np.arange(1,len(df)+1)
    
    all_data = pd.concat([all_data,df],ignore_index=True)

    # print(df)

    all_data.to_csv('historical_fiction_detailed.csv')

time.sleep(10)
driver.close()