# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 19:42:42 2024

@author: david
"""

import os

def find_invalid_files(directory_path):
    invalid_chars = ['*', ':', '<', '>', '?', '/', '|']
    invalid_files = []

    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            if any(char in filename for char in invalid_chars):
                invalid_files.append(os.path.join(root, filename))

    return invalid_files

if __name__ == "__main__":
    target_directory = "/path/to/your/directory"
    invalid_files_list = find_invalid_files(target_directory)

    if invalid_files_list:
        print("Invalid files found:")
        for invalid_file in invalid_files_list:
            print(invalid_file)
    else:
        print("No invalid files found.")
