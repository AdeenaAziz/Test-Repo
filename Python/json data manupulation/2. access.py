"accessing dict data from json:"

import json
json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data) #converts json to dict

print(data["name"])  # Output: John
print(data["age"])   # Output: 30
