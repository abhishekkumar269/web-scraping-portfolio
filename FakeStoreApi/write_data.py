import json
import requests
import pandas as pd

url = 'https://fakestoreapi.com/products'
response = requests.get(url)
response.status_code

data = response.json()
str_data = json.dumps(data, indent=4)


with open(f"data/sample.txt","w") as f:
    f.write(str_data)






















    


