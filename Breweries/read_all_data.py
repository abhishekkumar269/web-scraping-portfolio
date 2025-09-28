import numpy as np
import json

with open('Breweries/data/sample.txt','r+') as f:
    data = f.read()

str_api_data =json.load(data)
print(str_api_data)
