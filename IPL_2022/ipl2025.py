import requests
import pandas as pd
from bs4 import BeautifulSoup

import openpyxl

excel = openpyxl.Workbook()

print(excel.sheetnames)

sheet = excel.active

sheet.append(["sno","team","fun_rem","overses","total_ply"])

try:

    url = requests.get("https://www.iplt20.com/auction/2022")

    soup = BeautifulSoup(url.text,"lxml")

    auc_data = soup.find("table",class_="ih-td-tab w-100 auction-tbl")
    # print(auc_data)

    headers = []

    for i in auc_data.find_all("th"):
        headers.append(i.text)

    # sheet.append([headers])
    
    data = soup.find("tbody" ,id ="pointsdata")

    total_data = data.find_all("tr")

    sno = []
    team = []
    fund_rem =[]
    ovr_ply = []
    totl_ply = []

    for i in total_data:

        sno.append(i.find_all("td")[0].text)
        team.append(i.find_all("td")[1].text)
        fund_rem.append(i.find_all("td")[2].text)
        ovr_ply.append(i.find_all("td")[3].text)
        totl_ply.append(i.find_all("td")[4].text) 

    # d = {"sno":sno,"team":team,"fun_rem":fund_rem,"over_ply":ovr_ply,"totl_ply":totl_ply}
    # df = pd.DataFrame(d)
    # print(df)
    # df.to_csv("ipl_auction.csv")

    sheet.append([sno,team,fund_rem,ovr_ply,totl_ply])       
        
except Exception as e:
    print(e)

excel.save("IPL_AUCTION_2025.xlsx")



