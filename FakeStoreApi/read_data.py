import json
import pandas as pd

with open('data/sample.py','r+')as d:
    all_data = d.read()
    # print(all_data)
    # print(type(all_data),len(all_data))

all_load = json.loads(all_data)
print(all_data)
# print(type(all_load),len(all_load))


'''single element fetching'''
# print(all_load[1]['id'])
# print(all_load[0]['price'])

'''multi element fetching'''
# filter_data = []
id = []
title = []
price = []
category = []
description = []
image = []
rating = []
rating2=  []

for el in range(0,len(all_load)):
    id.append(all_load[el]['id'])
    price.append(all_load[el]['price'])
    title.append(all_load[el]['title'])
    category.append(all_load[el]['category'])
    description.append(all_load[el]['description'])
    image.append(all_load[el]['image'])
    rating.append(all_load[el]['rating']["rate"])
    rating2.append(all_load[el]['rating']["count"])

d = {
    'ID':id,
    'TITLE':title ,
    'PRICE':price,
    'CATEGORY':category,
    'DESCRIPTION':description,
    'IMAGE':image,
    'RATING':rating,
    'VOTE_PEOPLE':rating2
}

df = pd.DataFrame(d)
# new_df = df.style.hide(axis='index')
# print(new_df)
df.to_csv('products.csv',index=False)
