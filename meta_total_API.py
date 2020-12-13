import requests
import json


urlLimitNumber = "5"
url = "https://api.fda.gov/food/enforcement.json?search=report_date:[20201201+TO+20201202]&limit=" + urlLimitNumber

response = requests.get(url)
data = response.text
parsed = json.loads(data)

meta_total_dict = parsed["meta"]["results"]["total"]

meta_total_json = json.dumps(meta_total_dict)
