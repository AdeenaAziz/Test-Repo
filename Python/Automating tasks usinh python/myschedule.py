import schedule
import time

def job():
    print("This is a scheduled task")

schedule.every().day.at("14:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
