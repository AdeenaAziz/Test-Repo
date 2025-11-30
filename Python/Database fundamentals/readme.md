This guide covers fundamental database concepts, relational models, and SQL basics essential for DevOps professionals.

🗄️ What is a Database?
A database is a structured collection of data organized in a way that it can be easily:

Accessed
Managed
Updated

Think of it as a container that holds categorized data in an organized manner.

🔗 Relational Models
Relational models organize data in tables with rows and columns, similar to Excel spreadsheets.

Tables = Relations
Rows   = Tuples  
Columns = Attributes
🔑 Database Keys
Primary Key
-- Example: Employees Table
+-------------+---------------+--------------+------------+
| EmployeeID  | EmployeeName  | DepartmentID | Position   |
+-------------+---------------+--------------+------------+
| 1           | John Doe      | 1            | Manager    |
| 2           | Jane Smith    | 1            | Developer  |
| 3           | Bob Johnson   | 2            | Analyst    |
+-------------+---------------+--------------+------------+
-- Primary Key: EmployeeID (Unique for each employee)

Foreign Key:
-- Employees Table
+-------------+---------------+--------------+------------+
| EmployeeID  | EmployeeName  | DepartmentID | Position   |
+-------------+---------------+--------------+------------+
| 1           | John Doe      | 1            | Manager    |
| 2           | Jane Smith    | 1            | Developer  |
+-------------+---------------+--------------+------------+

-- Departments Table  
+--------------+----------------+
| DepartmentID | DepartmentName |
+--------------+----------------+
| 1            | Sales          |
| 2            | IT             |
+--------------+----------------+
-- Foreign Key: DepartmentID in Employees references Departments

Database Relationships:
1. One-to-One Relationship
-- Users Table
+---------+-----------+
| UserID  | Username  |
+---------+-----------+
| 1       | john_doe  |
| 2       | jane_smith|
+---------+-----------+

-- UserProfiles Table
+---------+----------+-----------+
| UserID  | FullName | Email     |
+---------+----------+-----------+
| 1       | John Doe | john@email|
| 2       | Jane Smith| jane@email|
+---------+----------+-----------+
