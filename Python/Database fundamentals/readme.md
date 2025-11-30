# What is a Database?
A structured collection of data organized for easy access, management, and updating
Acts as a centralized repository for organized data

## Relational Models
Way of organizing data in tables with rows and columns

**Table/Relation** = Collection of related data

**Rows/Tuples** = Horizontal entries

**Columns/Attributes** = Vertical categories

### Database Keys 
*Primary Key*
Unique identifier for each record in a table
Example: Employee ID (each employee has unique ID)
Cannot have duplicate values

*Foreign Key*
Column that references primary key in another table
Establishes relationships between tables
Example: Department ID in Employees table references Department table

**Database Relationships**
Three Types of Relationships:
>*One-to-One*: One record in Table A relates to exactly one record in Table B

> Example: User ↔ User Profile
USERS Table:
UserID | Username | Email
1      | john_doe | john@email.com
2      | jane_smith | jane@email.com

USER_PROFILES Table:
ProfileID | UserID | FullName       | Phone       | DateOfBirth
1         | 1      | John Doe       | 123-4567    | 1990-05-15
2         | 2      | Jane Smith     | 987-6543    | 1992-08-20

> *One-to-Many*: One record in Table A relates to multiple records in Table B

> Example: Department ↔ Multiple Employees

> *Many-to-Many*: Multiple records in Table A relate to multiple records in Table B

> Example: Students ↔ Courses (requires junction table)

### Normalization
Process of organizing database to minimize redundancy
Breaking large tables into smaller, related tables
Benefits: Easier management, reduced data duplication
Example: Split Customer Orders table into Customers and Orders tables

### SQL (Structured Query Language)
Domain-specific language for managing relational databases

Used for creating, retrieving, updating, and deleting data

**Common commands: SELECT, INSERT, UPDATE, DELETE, CREATE**




