import requests
from bs4 import BeautifulSoup


try:

    source = requests.get("https://www.iplt20.com/auction/2022")
    source.raise_for_status()

    soup = BeautifulSoup(source.text,"html.parser")


    headers = soup.find("table" ,class_="ih-td-tab w-100 auction-tbl").find_all("th")



    for title in headers:


        # print([title.text])

        pass
        

    values = soup.find("tbody",id="pointsdata").find_all("tr")

    for value in values:
        
        sno = value.find("tbody",id="pointsdata")

        sno = value.text.split()[0]
        overseas_pl= value.text.split()[3]
        totl_pl= value.text.split()[4]
        team = value.find("td",class_="ih-t-color").text
        print(sno,overseas_pl,totl_pl)




except Exception as e:
    print(e)    