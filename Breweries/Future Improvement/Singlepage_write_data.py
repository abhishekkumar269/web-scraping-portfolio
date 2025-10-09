import requests

import json

try:

    url = f'https://api.openbrewerydb.org/v1/breweries/?page=1'
    response = requests.get(url)
    data = response.json()
    api_format_data = json.dumps(data,indent=4)
    str1 = api_format_data

    with open('Breweries/data/sample.txt','w') as f :
        f.write(str1)

except Exception as e:
    print(e)
    







        



3.





