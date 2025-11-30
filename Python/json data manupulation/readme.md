# JSON Manipulation in Python - Complete Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Basic Operations](#basic-operations)
3. [File Operations](#file-operations)
4. [Practical Examples](#practical-examples)
5. [Practice Exercises](#practice-exercises)

---
```
## Introduction
JSON (JavaScript Object Notation) is a lightweight data format perfect for data exchange between Python and other systems.
import json

2. Creating JSON Data

# JSON as string
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# JSON from Python dictionary
python_dict = {
    "name": "John", 
    "age": 30, 
    "city": "New York"
}
3. Parsing JSON to Dictionary

json_data = '{"name": "John", "age": 30, "city": "New York"}'
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

**File Operations**
**Writing to JSON File**

with open("output.json", "w") as file:
    json.dump(data, file)

What happens:
Creates a new file called output.json
Writes your Python dictionary as proper JSON format
File contains: {"name": "John", "age": 28, "city": "New York", "country": "USA"}

**Reading from JSON File**
with open("output.json", "r") as file:
    data = json.load(file)
    print(data)


