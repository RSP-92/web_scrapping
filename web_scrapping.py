# Plan: 1) Use the BLS Public Data API to get JSON data of labor data
# 2) Clean and organize the data into a sql table 
# 3) Make a pipeline for the cleaned data
# #Later, use beautiful soup to scrap CDC data, see if there's cross over between two data sets  

import requests 
import json

#Making API Call
#Series IDs to call
#CEU6562160001 CEU6562160002 CEU6562160003 
#CEU6562160010 CEU6562160011 
url = 'https://api.bls.gov/publicAPI/v1/timeseries/data/CEU6562160001'
headers = {'Content-type': 'application/json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()
readable_file = 'data/readable_employee_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

#Print and analyze results



#It was a success!




