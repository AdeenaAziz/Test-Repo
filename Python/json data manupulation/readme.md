# JSON Manipulation in Python – Complete Guide

##  Project Overview  
A comprehensive guide to working with JSON in Python: from basic operations to file I/O, real-world examples, and hands-on exercises.  
This repository aims to help beginners and intermediates understand how to create, parse, manipulate, and persist JSON data using Python’s built-in `json` module.

##  Table of Contents  
- [Introduction](#introduction)  
- [Prerequisites](#prerequisites)  
- [Usage Examples](#usage-examples)  
  - [Creating JSON Data](#creating-json-data)  
  - [Parsing JSON Strings](#parsing-json-strings)  
  - [Accessing & Modifying Data](#accessing--modifying-data)  
  - [File Operations](#file-operations)  

## Introduction  
JSON (JavaScript Object Notation) is a widely used data-interchange format — readable for both humans and machines.  
Python’s built-in `json` module makes it effortless to handle JSON: parse, modify, and store JSON data.  
This guide walks through essential JSON operations in Python, with examples and exercises to help you learn by doing.

## Prerequisites  
- Python 3.x installed (preferably 3.6 or higher)  
- Basic familiarity with Python (variables, dictionaries, file I/O)  
- A code editor or IDE (VS Code, PyCharm, etc.)

## Usage Examples  

### Creating JSON Data  
```python
import json

# JSON as a string
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Or from a Python dictionary
python_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
#Parsing JSON Strings
data = json.loads(json_data)
print(data)  # {'name': 'John', 'age': 30, 'city': 'New York'}

#Accessing & Modifying Data
print(data["name"])  # John  
data["age"] = 28    # update  
data["country"] = "USA"  # add new key  

#File Operations
###Writing to JSON file
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)


###Reading from JSON file
with open("output.json", "r") as f:
    data = json.load(f)
print(data)

Reading from JSON file

with open("output.json", "r") as f:
    data = json.load(f)
print(data)
