#!/usr/bin/env python3
import os
import sys

# Check if a keyword is provided
if len(sys.argv) < 2:
    print("Usage: {} <keyword>".format(sys.argv[0]))
    sys.exit(1)

keyword = sys.argv[1]

# Loop through each directory in the PATH variable
directories = os.environ['PATH'].split(':')
for directory in directories:
    # Search for executables matching the keyword in each directory
    matches = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.access(file_path, os.X_OK) and keyword in file:
                matches.append(file_path)

    # Display the matches for the current directory
    if matches:
        print("Matches in {}:".format(directory))
        for idx, match in enumerate(matches, start=1):
            print("{:<5} {}".format(idx, match))
        print()
