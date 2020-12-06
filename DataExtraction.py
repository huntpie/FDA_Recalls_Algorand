import requests
import json
import csv

url = "https://api.fda.gov/drug/event.json?limit=1"

response = requests.get(url)

data = response.text

parsed = json.loads(data)
brand_name = parsed["results"][0]["patient"]["drug"][3]["openfda"]["brand_name"][0]


with open('output2.csv', 'w+') as f:
    f.write("Brand Name: " + brand_name)
