import smtplib
from email.mime.text import MIMEText

# -----------------------------
# Email Details
# -----------------------------
sender = "youremail@gmail.com"
receiver = "receiver@gmail.com"
subject = "Automated Email"
message = "Hello, this is an automated message"

# -----------------------------
# Connect to Gmail Server
# -----------------------------
server = smtplib.SMTP("smtp.gmail.com", 587)  # Gmail server and TLS port
server.starttls()  # Start TLS encryption

# -----------------------------
# Login Using App Password
# -----------------------------
# You cannot use your normal Gmail password.
# Go to Google Account → Security → App Passwords and generate a password.
server.login(sender, "your-app-password")  # Replace with your App Password

# -----------------------------
# Send Email
# -----------------------------
server.sendmail(sender, receiver, message)
server.quit()

print("Email sent successfully!")
