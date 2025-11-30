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

### Quick Start:
```python
import json

with open("output.json", "w") as file:
    json.dump(data, file)
