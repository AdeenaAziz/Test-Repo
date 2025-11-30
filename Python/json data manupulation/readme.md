# JSON Manipulation in Python - Complete Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Basic Operations](#basic-operations)
3. [File Operations](#file-operations)
4. [Practical Examples](#practical-examples)
5. [Practice Exercises](#practice-exercises)

---

## Introduction

JSON (JavaScript Object Notation) is a lightweight data format perfect for data exchange between Python and other systems.

### :
```python
import json

#creating json
#JSON as string
json_data = '{"name": "John", "age": 30, "city": "New York"}'

#JSON from Python dictionary
python_dict = {
    "name": "John", 
    "age": 30, 
    "city": "New York"
}

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

