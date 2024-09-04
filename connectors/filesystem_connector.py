import os

def fetch_data_from_filesystem(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data
