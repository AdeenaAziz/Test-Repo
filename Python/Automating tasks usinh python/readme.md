# Python Automation Scripts

This repository contains Python scripts for automating common tasks used in real-world corporate environments.

## Table of Contents

- Send Automated Emails
- Rename Files
- Delete Old Files
- Web Scraping
- Schedule Tasks
- Shutdown Computer
- Installation
- Usage

## Send Automated Emails

This script sends email notifications automatically using Gmail.

**Requirements**
- Python smtplib and email modules (built-in)
- Gmail account with App Password

**Steps**
- Import libraries: smtplib, MIMEText
- Define sender, receiver, message, and subject
- Connect to Gmail SMTP server (smtp.gmail.com) with TLS
- Login using App Password
- Send email

**Important:** Do NOT use your Gmail password. Use App Passwords from Google Account → Security → App Passwords.

## Rename Files

This script renames multiple files in a folder automatically.

**Requirements**
- Python os module (built-in)

**Steps**
- Import os
- Set the directory path
- Loop through files and rename them
- Replace old names with new names

**Example:** old_file1.txt → new_file1.txt

## Delete Old Files

This script deletes files older than a certain date.

**Requirements**
- Python os and datetime modules

**Steps**
- Import os and datetime
- Set the directory path
- Define a threshold date
- Loop through files and delete old ones

## Web Scraping

This script extracts all links from a website.

**Requirements**
- requests module
- beautifulsoup4 module

**Steps**
- Import requests and BeautifulSoup
- Get HTML of the website
- Parse HTML to find all <a> tags
- Extract href links

**Example:** Extract URLs from https://www.netflix.com

## Schedule Tasks

This script runs tasks at a specific time.

**Requirements**
- schedule and time modules

**Steps**
- Define a Python function to run
- Use schedule.every().day.at("HH:MM").do(function)
- Keep the script running with while True

**Example:** Print task at 2 PM every day.

## Shutdown Computer

This script shuts down a Windows computer.

**Requirements**
- Python os module

**Steps**
```python
import os
os.system("shutdown /s /t 0")
