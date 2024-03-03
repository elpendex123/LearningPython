import os
import random

# Function to create random empty files with sequential digits and specific extensions
def create_random_files(file_type):
    # Randomly determine the count between 5 and 10
    count = random.randint(5, 10)
    
    # Loop to create the specified number of files
    for i in range(1, count + 1):
        # Generate a sequential file name
        file_name = f"file_{file_type}_{i:03d}"
        # Create the full path for the file in the Downloads folder
        # file_path = os.path.join(downloads_path, f"{file_name}.{file_type}")
        file_path = os.path.join(os.path.expanduser(downloads_path), f"{file_name}.{file_type}")
        # Create an empty file by opening it in write mode and immediately closing it
        with open(file_path, 'w'):
            pass

# Path to the Downloads folder
downloads_path = "G:\git\LearningPython\temp"

# Create random empty files with sequential digits and specific extensions
create_random_files("txt")
create_random_files("mp3")
create_random_files("mp4")
create_random_files("jpg")
create_random_files("pdf")

print("Random empty files created in Downloads folder.")
