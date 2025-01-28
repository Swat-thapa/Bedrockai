import pandas as pd
import requests
import os

# Function to download file from URL
def download_file(url, destination_folder, filename):
    try:
        # Send GET request to download the file
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses (4xx or 5xx)

        # Ensure destination folder exists
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Path to save the file
        file_path = os.path.join(destination_folder, filename)

        # Write the content to the file
        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"File '{filename}' downloaded successfully at '{destination_folder}'")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file from {url}: {e}")

# Function to find the URL from CSV based on the file name
def get_file_url_from_csv(csv_file, file_name):
    try:
        # Load CSV into pandas DataFrame
        df = pd.read_csv(csv_file)

        # Check if columns exist
        if 'file_name' not in df.columns or 'url' not in df.columns:
            print("CSV is missing required columns: 'file_name' and 'url'.")
            return None

        # Find the row corresponding to the input file name
        file_row = df[df['file_name'] == file_name]

        # If file name is found, return the URL, otherwise return None
        if not file_row.empty:
            return file_row['url'].values[0]
        else:
            print(f"File name '{file_name}' not found in the CSV.")
            return None

    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None

# Main function to download the file based on user input
def download_file_from_github(csv_file, destination_folder):
    # Get user input for the file name
    file_name = input("Enter the file name you want to download: ")

    # Get the URL corresponding to the file name from the CSV
    url = get_file_url_from_csv(csv_file, file_name)

    if url:
        # Download the file if URL was found
        download_file(url, destination_folder, file_name)

# Example usage
if __name__ == '__main__':
    # Path to the CSV file containing file names and URLs
    csv_file = 'https://raw.githubusercontent.com/Swat-thapa/Bedrockai/refs/heads/main/workflows.csv'  # Adjust this path if necessary

    # Folder to save the downloaded files
    destination_folder = 'D:\workflows'

    download_file_from_github(csv_file, destination_folder)