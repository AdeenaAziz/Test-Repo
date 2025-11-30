Python Automation Scripts
This repository contains Python scripts for automating common tasks used in real-world corporate environments. These scripts help save time by automating repetitive tasks like sending emails, renaming files, deleting old files, scraping websites, scheduling tasks, and even shutting down your computer.

Table of Contents
Send Automated Emails

Rename Files

Delete Old Files

Web Scraping

Schedule Tasks

Shutdown Computer

Installation

Usage

Send Automated Emails
This script sends email notifications automatically using Gmail.

Requirements:

Python smtplib and email module (built-in)

Gmail account with App Password

Steps:

Import libraries: smtplib, MIMEText

Define sender, receiver, message, and subject

Connect to Gmail SMTP server (smtp.gmail.com) with TLS

Login using App Password

Send email

Important: Do NOT use your Gmail password. Use App Passwords from Google Account → Security → App Passwords.

Rename Files
This script renames multiple files in a folder automatically based on a naming convention.

Requirements: Python os module (built-in)

Steps:

Import os

Set the directory path

Loop through files and rename them

Replace old names with new names as required

Example: old_file1.txt → new_file1.txt

Delete Old Files
This script deletes files older than a certain date automatically.

Requirements: Python os and datetime modules (built-in)

Steps:

Import os and datetime

Set the directory path

Define a threshold date

Loop through files, check modification time, and delete files older than threshold

Web Scraping
This script extracts all links from a website.

Requirements:

requests module

beautifulsoup4 module

Steps:

Import requests and BeautifulSoup

Get HTML of the website

Parse HTML to find all <a> tags

Extract href links

Example: Extract all URLs from https://www.netflix.com

Schedule Tasks
This script runs tasks at a specific time automatically.

Requirements: schedule and time modules

Steps:

Define a Python function to run

Use schedule.every().day.at("HH:MM").do(function)

Keep the script running with while True

Example: Print "This is a scheduled task" at 2 PM every day.

Shutdown Computer
This script shuts down a Windows computer automatically.

Requirements: Python os module

Steps:

python
import os
os.system("shutdown /s /t 0")
/s → shutdown

/t 0 → immediately

⚠️ Be careful! This will shut down your computer immediately.

Installation
bash
pip install requests beautifulsoup4 schedule
Usage
Clone this repository

Install required dependencies

Run any script: python script_name.py

Modify variables according to your needs

