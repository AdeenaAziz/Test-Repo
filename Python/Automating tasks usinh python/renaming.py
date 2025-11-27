import os

# Path of the folder where files are stored
path = "C:/Users/YourFolder"

# Loop through each file in the folder
for filename in os.listdir(path):
    
    # Only rename files that end with .txt
    if filename.endswith(".txt"):
        
        # Create the new file name by replacing old_ with new_
        new_name = filename.replace("old_", "new_")
        
        # Rename the file
        os.rename(
            os.path.join(path, filename),     # old file path
            os.path.join(path, new_name)      # new file path
        )

print("Renaming completed!")
