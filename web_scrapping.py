# Plan: 1) Use the BLS Public Data API to get JSON data of labor data
# 2) Clean and organize the data into a sql table 
# 3) Make a pipeline for the cleaned data
# #Later, use beautiful soup to scrap CDC data, see if there's cross over between two data sets  

import requests 

#Making API Call

url = 'https://api.bls.gov/publicAPI/v1/timeseries/data/'
headers = {'Content-type': 'application/json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()

#Print and analyze results
print(response_dict.keys())


#It was a success!

for i in response_dict.keys():
    print(response_dict.values)

