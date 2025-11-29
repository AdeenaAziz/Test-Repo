import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)  # converts json to dict

# Adding new key-value pair
data["country"] = "USA"

# Updating existing data  
data["age"] = 28

#print("Updated dictionary:", data)


# THEN: READ from file
with open("output.json", "r") as file:
    loaded_data = json.load(file)
    print("Data from file:", loaded_data)