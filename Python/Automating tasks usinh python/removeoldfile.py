import os
import datetime

# Folder path where the files are located
path = "C:/Users/YourFolder"

# Set the date limit — files older than this will be deleted
threshold_date = datetime.datetime(2023, 10, 1)

# Go through every file in the folder
for file in os.listdir(path):

    # Get the full path of the file
    file_path = os.path.join(path, file)

    # Get the file's last modified time
    file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

    # If file is older than threshold date → delete it
    if file_time < threshold_date:
        os.remove(file_path)
        print(f"Deleted: {file}")

print("Old file cleanup completed!")
