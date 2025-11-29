i) Summary of JSON Manipulation in Python:
1. Importing JSON Library

import json
2. Creating JSON Data

json_data = '{"name": "John", "age": 30, "city": "New York"}'
3. Parsing JSON to Dictionary

data = json.loads(json_data)
print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
4. Accessing JSON Data

print(data["name"])  # Output: John
print(data["age"])   # Output: 30
5. Modifying JSON Data

# Adding new key-value pair
data["country"] = "USA"

# Updating existing data
data["age"] = 28

print(data)  # Shows updated dictionary

ii) Converting Dictionary to JSON String

updated_json_data = json.dumps(data)
print(updated_json_data)  # JSON formatted string

iii) Writing to JSON File

with open("output.json", "w") as file:
    json.dump(data, file)

  e.g.:
Think of it like saving a document on your computer. You take what's in your Python program and save it as a file.


import json

# Your data in Python
data = {
    "name": "John",
    "age": 28,
    "city": "New York",
    "country": "USA"
}

# Save this data to a file
with open("output.json", "w") as file:
    json.dump(data, file)
What happens:
Creates a new file called output.json

Writes your Python dictionary as proper JSON format
The file will contain:
{"name": "John", "age": 28, "city": "New York", "country": "USA"}

iv) Reading from JSON File
 
with open("output.json", "r") as file:
    data = json.load(file)
    print(data)


e.g.:

import json

# STEP 1: Create some data
user_profile = {
    "username": "alice",
    "email": "alice@email.com",
    "preferences": {"theme": "dark", "language": "en"}
}

# STEP 2: Save it to a file (like saving game progress)
print("Saving data to file...")
with open("user_profile.json", "w") as file:
    json.dump(user_profile, file)

# STEP 3: Later, load it back (like loading saved game)
print("Loading data from file...")
with open("user_profile.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded data:", loaded_data)