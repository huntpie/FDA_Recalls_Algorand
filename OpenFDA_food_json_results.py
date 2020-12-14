import requests
import json
import meta_total_API

# pull metal_total_json from meta_total_API
urlLimitNumber = meta_total_API.meta_total_json
url = "https://api.fda.gov/food/enforcement.json?search=report_date:[20201201+TO+20201202]&limit=" + urlLimitNumber

# dump request to JSON
response = requests.get(url)
data = response.text

# parse JSON from total results - starts at 0, so if 13 results it would be 0-12
parsed = json.loads(data)

# remove unwanted data fields to compress JSON to under 1KB to fit in notefield
for x in range(0, int(meta_total_API.meta_total_json)):
    all_results_dict = parsed["results"][x]
    entries_to_remove = ('event_id', 'openfda',
                         'initial_firm_notification', 'address_2')
    for k in entries_to_remove:
        all_results_dict.pop(k, None)

# loop each result into a dictionary based on the meta total from the API call
rde = {}
for y in range(1, int(meta_total_API.meta_total_json)):
    rde["results_dict_{}".format(
        y)] = parsed["results"][y]

# add string prefix of "FDAF" to represent FDA Food Recalls
results_json_1 = json.dumps(rde["results_dict_1"])


# test code to see if split to JSON worked correctly
print(results_json_1)


# side notes
# format date field of url to make solution more intuitive
#
