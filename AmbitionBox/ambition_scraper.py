from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav').text #scrapping allowed
# print(source)
#robot.txt(check any websites status scrapping is avalible or not)

driver=webdriver.Chrome()


# webpage = driver.get('https://www.ambitionbox.com/list-of-companies?campaign=homepage_explore_companies_widget&page=1')

# for i in range(2,5):#failed
    #     webpage = driver.get('https://www.ambitionbox.com/list-of-companies?page={}'.format(i))
    #     time.sleep(5)

    # soup = BeautifulSoup(webpage,'lxml') #didn't work out selenium+beautyfulsoup combo

    # all_h1 = soup.find_all('h1')
    # print(len(all_h1))

    # h2 = driver.find_element(By.TAG_NAME,"h2").text
    # print(h2) 

    # h2 = driver.find_elements(By.TAG_NAME,"h2") #return in form of LIST
    # print(len(h2))

    # for name in h2:
    #     print(name.text) #use strip() to remove spaces
    # ratings = driver.find_elements(By.XPATH,"//*[@style='height:auto;padding-bottom:1px;']")

    # for rating in ratings:
    #     print(rating.text)

    # all_p = driver.find_element(By.TAG_NAME,"p")
    # print(all_p.text)

    # all_a = driver.find_elements(By.TAG_NAME,"a")
    # for a in all_a:
    #     print(a.text.strip)

    # all_company = driver.find_elements(By.XPATH,"//*[@class='companyCardWrapper']") #failed to achieve result
    # print(len(all_company))

#     '''main code'''

# final = pd.DataFrame()

# for i in range(1,10):

#     driver.find_element(By.XPATH,"//*[@class='icon-chevron-right next nav-btn']").click()
#     time.sleep(5)

#     all_company =driver.find_elements(By.XPATH,"//*[@class='companyCardWrapper__companyPrimaryDetailsTopSection']")
#     all_review = driver.find_elements(By.XPATH,"//*[@class='rating_star_container']")
#     all_rating_count = driver.find_elements(By.XPATH,"//*[@class='companyCardWrapper__companyRatingCount']")
#     all_info = driver.find_elements(By.XPATH,"//span[@class='companyCardWrapper__interLinking']")

#     name = []
#     review_lis = []
#     rating_count = []
#     company_type = []
#     com_hq = []

#     for company in all_company:
#         name.append(company.text)
        
#     for review in all_review:
#         review_lis.append(review.text)

#     for rating in all_rating_count:
#         rating_count.append(rating.text)

#     for info in all_info:
#         company_type.append(info.text.split('|')[0])
#         com_hq.append(info.text.split('|')[1])
        
#     # print(name,review_lis,rating_count,company_type,com_hq)
#     d = {'NAME':name,'REVIEW':review_lis,'NO_OF_PEOPLE_RATINGS':rating_count,'COMAPANY TYPE':company_type,'COMANY_HEADQUARTES':com_hq}
#     df = pd.DataFrame(d)
    # print(df.shape)

    # final.append(df)
    # df.to_csv("company_details.csv")



final = []
for i in range(1,3):
        
        webpage = driver.get('https://www.ambitionbox.com/list-of-companies?page={}'.format(i))
        time.sleep(5)


        all_company =driver.find_elements(By.XPATH,"//*[@class='companyCardWrapper__companyPrimaryDetailsTopSection']")
        all_review = driver.find_elements(By.XPATH,"//*[@class='rating_star_container']")
        all_rating_count = driver.find_elements(By.XPATH,"//*[@class='companyCardWrapper__companyRatingCount']")
        all_info = driver.find_elements(By.XPATH,"//span[@class='companyCardWrapper__interLinking']")

        name = []
        review_lis = []
        rating_count = []
        company_type = []
        com_hq = []

        for company in all_company:
            name.append(company.text)
        
        for review in all_review:
            review_lis.append(review.text)

        for rating in all_rating_count:
            rating_count.append(rating.text)

        for info in all_info:
            company_type.append(info.text.split('|')[0])
            com_hq.append(info.text.split('|')[1])

        d = {'NAME':name,'REVIEW':review_lis,'NO_OF_PEOPLE_RATINGS':rating_count,'COMAPANY TYPE':company_type,'COMANY_HEADQUARTES':com_hq}
        df = pd.DataFrame(d)
        final.append(df)
print(final)
df.to_csv('company_details.csv')

time.sleep(5)
driver.close()

