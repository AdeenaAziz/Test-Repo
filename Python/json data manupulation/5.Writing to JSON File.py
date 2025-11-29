import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data) #converts json to dict

# Adding new key-value pair
data["country"] = "USA"

# Updating existing data
data["age"] = 28

#print(data)  # Shows updated dictionary

#updated_json_data = json.dumps(data)
#print(updated_json_data)  # JSON formatted string


with open("output.json", "w") as file:
    json.dump(data, file)