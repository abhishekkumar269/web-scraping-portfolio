import requests
import pandas as pd
from bs4 import BeautifulSoup


try:

    source = requests.get("https://www.tutorialsfreak.com/")
    source.raise_for_status

    # print(source.content)

    # print(source.url)

    # print(source.status_code)

    soup = BeautifulSoup(source.content,"lxml")

    # print(soup.prettify())

    # print(soup.title.text)

    # print(soup.a)

    # print(soup.h2)

    # print(soup.p)

    # tag = soup.html

    # # print(type(tag))

    # tag = soup.a

    # print(tag)

    # tag = soup.h3

    # print(tag)

    # tag = soup.h1.string

    # print(tag)

    # tag = soup.p.string

    # print(tag)

    # print(soup.title)

    # print(soup.find("h1"))

    # print(soup.find_all("h1"))

    # print(soup.find("p"))

    # print(soup.find_all("p"))

    # print(soup.p.string)#comment checking


    # class_data = soup.find("h3",class_="fs-20 lh-30 fw-600 label-color-5")

    # print(class_data)

    # id_data = soup.find("div",id="__next").text

    # print(id_data)


    # content = soup.find("div" ,class_="why-choose-card card-shadow card")

    # for i in content.find("h3",class_=""):



    # ny  = soup.find_all('div', class_="why-choose-card card-shadow card")

    # for head in ny:
    #     head.find_all('h3',class_="fs-20 lh-30 fw-600 label-color-5")

    # print(head.text)


    link = []

    for i in soup.find_all("a"):
        link.append(i.get("href"))

    data = {"link":link}

    df = pd.DataFrame(data)
    df.to_csv("tutioral.csv")



    image = []

    for i in soup.find_all("img"):
        image.append(i.get("src"))

    data2 = {"image":image}

    df = pd.DataFrame(data2)
    print(df)

    df.to_csv("imgage.csv")


  

    print(df)












except Exception as e:

    print(e)