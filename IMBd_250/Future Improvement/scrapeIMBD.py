from bs4 import BeautifulSoup

import requests, openpyxl

excel = openpyxl.Workbook()

print(excel.sheetnames)

sheet =excel.active

sheet.title='Top rared movie'

print(excel.sheetnames)

sheet.append(['Rank of movie','Name of move','Year of relase','ImbdRatings'])


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

try:
    url = "https://www.imdb.com/chart/top/"

    source = requests.get(url,headers=headers)

    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')

    movies = soup.find('ul' , class_ = 'ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM compact-list-view ipc-metadata-list--base').find_all('li')

    for movie in movies:

        rank = movie.find('h3',class_='ipc-title__text').get_text(strip=True).split('.')[0]
        
        name = movie.find('h3',class_='ipc-title__text').get_text(strip=True).split('.')[1]

        year = movie.find('span',class_='sc-5179a348-7 idrYgr cli-title-metadata-item').text

        ratings = movie.find('span',class_='ipc-rating-star--rating').text


        sheet.append([rank,name,year,ratings])
    

except Exception as e:

    print(e)

excel.save('IMbd movie.xlsx')




# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# import time

# gecko_driver_path = r"D:\Python\WEB SCRAPING\geckodriver.exe"

# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.set_preference("general.useragent.override","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0")

# service = Service(executable_path=gecko_driver_path)
# driver = None