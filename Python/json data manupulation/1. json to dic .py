import json
json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

