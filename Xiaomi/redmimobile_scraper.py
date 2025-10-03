import requests
from bs4 import BeautifulSoup
import pandas as pd

try:

    response = requests.get("https://www.mi.com/in/product-list/redmi/?srsltid=AfmBOooYrcAUC9dsFB-0kTlIOf_zUy7Spszcaq01eGLf40ZpvEtP5m07")
    response.raise_for_status()

    soup = BeautifulSoup(response.text,"lxml")
    # print(soup.prettify())

    # for i in soup.find_all("h3"):
        
    #     print(i.text)

    # for i in soup.find_all("span",class_="comment__label"):
    #     print(i.text)


    all_product = soup.find("ul" , class_="mi-product__list")

    item = all_product.find_all("li")


    name = []
    price = []
    review = []
    memory = []

    for i in item:

        name.append(i.find('h3',class_="item__title").text)
        # price.append(i.find('small',class_="mi-product__item-wrapper").text)
        # review.append(i.find('div',class_='mi-marketing-label__comment item__marketing-text').text)
        # memory.append(i.find('span',class_='selector__label selector__label--active').text)

    d = {"name":name}

    df = pd.DataFrame(d)
    print(df)

    df.to_csv("mi_data.csv")
    

except Exception as e:
    print(e)