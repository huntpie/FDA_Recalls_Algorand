import requests
import json
import csv

url = "https://api.fda.gov/food/enforcement.json?search=report_date:[20201201+TO+20201202]&limit=100"

response = requests.get(url)

data = response.text

parsed = json.loads(data)
results_country = parsed["results"][0]["country"]
results_city = parsed["results"][0]["city"]


with open('FDA20201201to20201202.csv', 'w+') as f:
    f.write("Country: " + results_country + ", City: " + results_city)
