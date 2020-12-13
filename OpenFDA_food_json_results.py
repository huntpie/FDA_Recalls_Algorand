import base64
import requests
import json
from itertools import islice
import meta_total_API

# pull metal_total_json from meta_total_API
urlLimitNumber = meta_total_API.meta_total_json
url = "https://api.fda.gov/food/enforcement.json?search=report_date:[20201201+TO+20201202]&limit=" + urlLimitNumber

# first check meta total results from API request
#print("Total results for API Request Date = " + meta_total_API.meta_total_json)

# dump request to JSON
response = requests.get(url)
data = response.text


# parse JSON from total results - starts at 0, so if 13 results it would be 0-12
parsed = json.loads(data)
results_dict_1 = parsed["results"][0]
results_dict_2 = parsed["results"][1]
results_dict_3 = parsed["results"][2]
results_dict_4 = parsed["results"][3]
results_dict_5 = parsed["results"][4]
results_dict_6 = parsed["results"][5]
results_dict_7 = parsed["results"][6]
results_dict_8 = parsed["results"][7]
results_dict_9 = parsed["results"][8]
results_dict_10 = parsed["results"][9]
results_dict_11 = parsed["results"][10]
results_dict_12 = parsed["results"][11]
results_dict_13 = parsed["results"][12]

# split one Recall results dictionaries into two due to data size
inc = iter(results_dict_1.items())
results_split_1 = dict(islice(inc, len(results_dict_1) // 2))
results_split_2 = dict(inc)

# add prefix that labels the split and the date of API Search. EX: 20201201-02:1:1 ; 20201201-02:2:1
# 20201201-02 represents the API call date and the following :1 equals the first result of the JSON request
# the follow :1 equals the first half of the result
# for instance 20201201-02:12:2 equals date of December 1st - 2nd 2020, 12th result, 2nd split of data


# convert split dictionaires to JSON strings
results_json_1 = json.dumps(results_split_1)
results_json_2 = json.dumps(results_split_2)

# test code to see if split to JSON worked correctly
print(results_json_1)
print(results_json_2)

# side notes
# format date field of url to make solution more intuitive
#
