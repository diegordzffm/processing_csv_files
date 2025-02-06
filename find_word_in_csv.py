'''import os

def find_consumption_in_csv(folder_path):
  """
  This function checks if the word "consumption" is found in any CSV files within a folder.

  Args:
      folder_path: The path to the folder containing the CSV files.
  """
  for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
      file_path = os.path.join(folder_path, filename)
      found = False
      # Open the CSV file in read mode
      with open(file_path, 'r') as csvfile:
        # Iterate through each line (row) in the CSV
        for row in csvfile:
          # Convert the row to lowercase for case-insensitive search
          if "consumption" in row.lower():
            found = True
            break  # Stop iterating if found

      if found:
        print(f"Found 'consumption' in file: {filename}")

# Replace 'path/to/your/folder' with the actual path to your folder containing CSV files
find_consumption_in_csv('20240331')'''


'''
import pandas as pd
import os

def find_consumption_in_folder(folder_path):
  """
  This function searches for the word "consumption" in CSV files within a folder.

  Args:
      folder_path: The path to the folder containing CSV files.
  """
  for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
      file_path = os.path.join(folder_path, filename)
      try:
        # Read the CSV file using pandas
        df = pd.read_csv(file_path)
        
        # Check if any cell contains "consumption" (case-insensitive)
        if "WCK".lower() in df.values.any():
          print(f"Found 'consumption' in file: {filename}")
      except Exception as e:
        print(f"Error reading file: {filename}. Exception: {e}")

# Specify the folder path containing your CSV files
folder_path = "20231231"
find_consumption_in_folder(folder_path)
'''

'''
import pandas as pd
import os

# Function to search for the word 'consumption' in a DataFrame
def search_word_in_dataframe(df, word='consumption', encoding='utf-8'):
    for col in df.columns:
        if df[col].dtype == object:
            matches = df[col].str.contains(word, na=False)
            if matches.any():
                rows = matches[matches].index.tolist()
                for row in rows:
                    print(f"Word '{word}' found in file '{file_path}' at row {row} and column '{col}'.")

# Function to read CSV files and search for the word
def read_and_search_csv_files(folder_path, word='consumption'):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            try:
                df = pd.read_csv(file_path, encoding='utf-8')
                search_word_in_dataframe(df, word)
            except Exception as e:
                print(f"Error reading file '{file_path}': {e}")

# Define the folder path
folder_path = '20240331'

# Execute the function
read_and_search_csv_files(folder_path)
'''

import os
import numpy as np


def check_consumption(folder_path, encoding='utf-8'):
  """
  This function checks for the word "consumption" in CSV files within a folder.

  Args:
    folder_path: Path to the folder containing the CSV files.
  """
  for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
      try:
        # Read data using numpy.genfromtxt
        data = np.genfromtxt(os.path.join(folder_path, filename), delimiter=",", dtype=None, encoding='utf-8')

        # Check if "consumption" is found (case-insensitive)
        if np.any(np.vectorize(lambda x: "consumption".lower() in str(x).lower())(data)):
          print(f"Found 'consumption' in file: {filename}")
      except Exception as e:
        # Print error details with filename and datapoint (if available)
        print(f"Error reading file: {filename}")
        try:
          # Attempt to print datapoint where error occurred (if data is loaded)
          if data is not None:
            print(f"Datapoint: {data[-1]} (assuming error at last line)")
        except:
          pass
        print(f"Error message: {e}")


if __name__ == "__main__":
  # Replace 'path/to/your/folder' with your actual folder path
  folder_path = "20240331"
  check_consumption(folder_path, encoding='utf-8')
