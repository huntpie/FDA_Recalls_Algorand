import base64
import requests
import json
from itertools import islice

url = "https://api.fda.gov/food/enforcement.json?search=report_date:[20201201+TO+20201202]&limit=1"

response = requests.get(url)

data = response.text

parsed = json.loads(data)
results_dict = parsed["results"][0]

inc = iter(results_dict.items())
results_split_1 = dict(islice(inc, len(results_dict) // 2))
results_split_2 = dict(inc)

results_json_1 = json.dumps(results_split_1)

print(results_json_1)


# with open('FDA20201201to20201202.csv', 'w+') as f:
# f.write("Country: " + results_country + ", City: " + results_city)
