Python Automation Scripts
This repository contains Python scripts for automating common tasks used in real-world corporate environments.
Table of Contents
•	Send Automated Emails
•	Rename Files
•	Delete Old Files
•	Web Scraping
•	Schedule Tasks
•	Shutdown Computer
•	Installation
•	Usage
________________________________________
Send Automated Emails
This script sends email notifications automatically using Gmail.
Requirements
•	Python smtplib and email modules (built-in)
•	Gmail account with App Password
Steps
1.	Import libraries: smtplib, MIMEText
2.	Define sender, receiver, message, and subject
3.	Connect to Gmail SMTP server (smtp.gmail.com) with TLS
4.	Login using App Password
5.	Send email
 Important: Do NOT use your Gmail password. Use App Passwords from Google Account → Security → App Passwords.
________________________________________
Rename Files
This script renames multiple files in a folder automatically.
Requirements
•	Python os module (built-in)
Steps
1.	Import os
2.	Set the directory path
3.	Loop through files and rename them
4.	Replace old names with new names
Example: old_file1.txt → new_file1.txt
________________________________________
Delete Old Files
This script deletes files older than a certain date.
Requirements
•	Python os and datetime modules
 Steps
1.	Import os and datetime
2.	Set the directory path
3.	Define a threshold date
4.	Loop through files and delete old ones
________________________________________
 Web Scraping
This script extracts all links from a website.
 Requirements
•	requests module
•	beautifulsoup4 module
 Steps
1.	Import requests and BeautifulSoup
2.	Get HTML of the website
3.	Parse HTML to find all <a> tags
4.	Extract href links
Example: Extract URLs from https://www.netflix.com
________________________________________
 Schedule Tasks
This script runs tasks at a specific time.
 Requirements
•	schedule and time modules
 Steps
1.	Define a Python function to run
2.	Use schedule.every().day.at("HH:MM").do(function)
3.	Keep the script running with while True
Example: Print task at 2 PM every day.
________________________________________
 Shutdown Computer
This script shuts down a Windows computer.
 Requirements
•	Python os module
 Steps
python
import os
os.system("shutdown /s /t 0")
•	/s = shutdown
•	/t 0 = immediately
 WARNING: This will shut down your computer immediately!
________________________________________
 Installation
bash
pip install requests beautifulsoup4 schedule________________________________________
🤝 Contributing
Feel free to contribute by submitting issues or pull requests!
 License
This project is open source and available under the MIT License.
________________________________________
Happy Automating! 🎉

