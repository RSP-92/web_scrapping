import requests 
import json
import pandas as pd
from pathlib import Path

def clean_data(pathway):
    p = Path(pathway)
    with p.open('r', encoding='utf-8') as f:
        data = json.loads(f.read())
    results_series = data['Results']['series']
    results_data = results_series[0]
    results_year = results_data['data']
    all_data = []

    for year in results_year:
        all_data.append(year)
    df = pd.DataFrame(all_data)
    print(df)
    return df


# print(type(results_series)) < returns a list
clean_data(r'data\readable_employee_data.json')


# print(type(results_data)) < returns a dict

# print(f"\n{results_data['data']}")



# print(f"\nThis is results year: {results_year}")

# print(type(results_year)) < returns a list, I'm noticing a pattern



    



#It worked!!!


# print(f"\nResults period: {results_period}") < returns smallest section of dict

#I don't know if making a function will make it better or worse, will




    
