# Database Basics & Relationships Guide

## Table of Contents
1. [Introduction to Databases](#introduction-to-databases)
2. [Relational Models](#relational-models)
3. [Database Keys](#database-keys)
4. [Database Relationships](#database-relationships)
5. [Normalization](#normalization)
6. [SQL Basics](#sql-basics)
7. [Examples & Use Cases](#examples--use-cases)

---

## Introduction to Databases

### What is a Database?
A database is a structured collection of data organized for easy access, management, and updating.

### Characteristics:
- Structured and organized data
- Centralized storage
- Supports multiple users
- Provides data security
- Ensures data integrity

---

## Relational Models

### Definition:
A way of organizing data in tables with rows and columns.

### Components:
| Term | Description | Example |
|------|-------------|---------|
| **Table/Relation** | Collection of related data | Employees table |
| **Rows/Tuples** | Horizontal entries | Individual employee records |
| **Columns/Attributes** | Vertical categories | Employee ID, Name, Department |

---

## Database Keys

### Primary Key
- Unique identifier for each record
- Must be unique and cannot be NULL
- Only one per table

### Foreign Key
- Creates relationship between tables
- References primary key of another table
- Can have duplicate values and can be NULL

---

## Database Relationships

### 1. One-to-One Relationship
One record in Table A relates to exactly one record in Table B.

**Examples**: 
- User ↔ User Profile
- Person ↔ Passport

### 2. One-to-Many Relationship
One record in Table A relates to multiple records in Table B.

**Examples**:
- Department ↔ Employees
- Customer ↔ Orders

### 3. Many-to-Many Relationship
Multiple records in Table A relate to multiple records in Table B.

**Examples**:
- Students ↔ Courses
- Doctors ↔ Patients

---

## Normalization
Process of organizing database structure to minimize redundancy and improve data integrity.

---

## SQL Basics
Structured Query Language for managing relational databases.

### Common Commands:
- `SELECT` - Retrieve data
- `INSERT` - Add new records
- `UPDATE` - Modify records
- `DELETE` - Remove records
- `CREATE` - Create tables

---

## Quick Start
Check the `examples/` directory for practical SQL examples and `practice/` for exercises.
