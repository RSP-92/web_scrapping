import requests 
import json
import pandas as pd
from pathlib import Path

p = Path(r'data\readable_employee_data.json')

with p.open('r', encoding='utf-8') as f:
    data = json.loads(f.read())

print(data)

results_series = data['Results']['series']

# print(type(results_series)) < returns a list

results_data = results_series[0]

# print(type(results_data)) < returns a dict

# print(f"\n{results_data['data']}")

results_year = results_data['data']

# print(f"\nThis is results year: {results_year}")

# print(type(results_year)) < returns a list, I'm noticing a pattern

for year in results_year:
    print(f"\n{year}")

results_period = year



# print(f"\nResults period: {results_period}") < returns smallest section of dict

#I don't know if making a function will make it better or worse, will try

