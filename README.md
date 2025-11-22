# Student Average Calculator (HackerRank Problem)

This project solves a common HackerRank Python problem:
**Given subject-wise marks of students, compute the average marks of each student.**

The input format provides marks **row-wise** (each row is a subject), but the output
requires average marks **column-wise** (each column is a student).  
To handle this, the solution uses Python’s `zip(*lists)` to transpose the data.

---

## 🧮 Problem Description

- The first input line contains:
n x
where  
**n = number of students**  
**x = number of subjects**

- The next **x lines** each contain the marks of all `n` students for that subject.

### Example Input

5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5

### Expected Output

90.0
91.0
82.0
90.0
85.5

## 🧠 Solution Logic

1. Read `n` and `x`
2. Read `x` rows of subject-wise marks
3. Use `zip(*marks)` to transpose rows → columns
4. Compute the average for each student
5. Print the results (one average per line)

---

## 📌 student_averages.py


HackerRank Problem:
Compute the average marks of each student given subject-wise input.

Input:
- First line: n (number of students), x (number of subjects)
- Next x lines: marks of n students for each subject

Output:
- Average marks of each student (one per line)
"""

# Read number of students and subjects
n, x = map(int, input().split())

# Read marks subject-wise
marks = []
for _ in range(x):
    course = list(map(float, input().split()))
    marks.append(course)

# Transpose and compute averages
for student_marks in zip(*marks):
    print(sum(student_marks) / x)





The end 
