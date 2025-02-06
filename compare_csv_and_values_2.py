'''import os
import pandas as pd

def compare_csv_files(folder1, folder2, filename):
  """
  Compares columns and values between two CSV files with the same filename.

  Args:
      folder1: Path to the first folder (CityA).
      folder2: Path to the second folder (CityB).
      filename: Name of the CSV files to compare.

  Returns:
      A dictionary containing information about column mismatches.
  """

  mismatches = {}

  # Get full paths to the CSV files
  file1_path = os.path.join(folder1, filename)
  file2_path = os.path.join(folder2, filename)

  try:
    # Read CSV files using pandas
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Check if column names are identical
    if not df1.columns.tolist() == df2.columns.tolist():
      mismatches["column_names"] = "Column names differ between files."

    # Compare corresponding columns
    for col in df1.columns:
      if col in df2:
        # Check if number of rows is the same
        if len(df1[col]) != len(df2[col]):
          mismatches[col] = "Different number of rows in column."
        else:
          # Compare values element-wise (excluding potential NaN values)
          mismatched_rows = (df1[col] != df2[col]).dropna().index.tolist()
          if mismatched_rows:
            mismatches[col] = f"Values differ at rows: {mismatched_rows}"
      else:
        mismatches[col] = f"Column '{col}' not found in second file."

  except FileNotFoundError:
    mismatches["error"] = f"File not found: {filename}"

  return mismatches

# Example usage (assuming 10 CSV files with the same name exist)
num_files = 10
filename = "L2_LOAN_DEPOSIT.csv"  # Replace with the actual filename

for i in range(1, num_files + 1):
  mismatches = compare_csv_files("20231231", "20240331", f"{filename}{i}")
  if mismatches:
    print(f"File '{filename}{i}':")
    for key, value in mismatches.items():
      print(f"\t- {key}: {value}")

      '''
'''
import os
import pandas as pd

def compare_csv_files(folder1, folder2):
  """
  Compares columns and rows of CSV files with the same name in two folders.

  Args:
      folder1: Path to the first folder (CityA).
      folder2: Path to the second folder (CityB).

  Returns:
      A dictionary containing information about mismatches for each file pair.
  """

  mismatches = {}
  for filename in os.listdir(folder1):
    # Check if file exists in both folders
    file2_path = os.path.join(folder2, filename)
    if os.path.isfile(file2_path):
      try:
        # Read CSV files using pandas
        df1 = pd.read_csv(os.path.join(folder1, filename))
        df2 = pd.read_csv(file2_path)

        # Compare number of rows
        if len(df1) != len(df2):
          mismatches[filename] = f"Different number of rows ({len(df1)} vs {len(df2)})."
        else:
          # Compare columns
          for col in df1.columns:
            if col in df2:
              # Compare values element-wise (excluding potential NaN values)
              mismatched_rows = (df1[col] != df2[col]).dropna().index.tolist()
              if mismatched_rows:
                mismatches[filename] = f"Values differ in column '{col}' at rows: {mismatched_rows}"
            else:
              mismatches[filename] = f"Column '{col}' not found in second file."

      except FileNotFoundError:
        mismatches[filename] = f"File not found: {filename}"
      except pd.errors.ParserError:
        mismatches[filename] = f"Error parsing CSV: {filename}"

  return mismatches

# Example usage
folder1 = "20231231"
folder2 = "20240331"

mismatches = compare_csv_files(folder1, folder2)

if mismatches:
  print("Mismatches found:")
  for filename, message in mismatches.items():
    print(f"\tFile: {filename}")
    print(f"\t\t- {message}")
else:
  print("No mismatches found between CSV files in 20231231 and 20240331.")
'''

'''
import pandas as pd
import os

def compare_csv_files(folder1, folder2, filename):
  """
  Compares columns, rows, and values between two CSV files.

  Args:
      folder1: Path to the first folder (CityA).
      folder2: Path to the second folder (CityB).
      filename: Name of the CSV files to compare.

  Returns:
      A dictionary containing information about mismatches.
  """

  mismatches = {}

  # Get full paths to the CSV files
  file1_path = os.path.join(folder1, filename)
  file2_path = os.path.join(folder2, filename)

  try:
    # Read CSV files using pandas
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Check if column names are identical
    if not df1.columns.tolist() == df2.columns.tolist():
      mismatches["column_names"] = "Column names differ between files."

    # Check if row counts are identical
    if len(df1) != len(df2):
      mismatches["rows"] = "Different number of rows in files."

    # Compare corresponding columns
    for col in df1.columns:
      if col in df2:
        # Compare values element-wise (excluding potential NaN values)
        mismatched_rows = (df1[col] != df2[col]).dropna().index.tolist()
        if mismatched_rows:
          mismatches[col] = f"Values differ at rows: {mismatched_rows}"
      else:
        mismatches[col] = f"Column '{col}' not found in second file."

  except FileNotFoundError:
    mismatches["error"] = f"File not found: {filename}"

  return mismatches

# Example usage
folder1 = "20231231"
folder2 = "20240331"
filename = "L2_LOAN_DEPOSIT.csv"

mismatches = compare_csv_files(folder1, folder2, filename)

if mismatches:
  print("Mismatches found:")
  for key, value in mismatches.items():
    print(f"\t- {key}: {value}")
else:
  print("The CSV files appear to be identical.")'''




'''

import os
import pandas as pd

def compare_csv_files(folder1, folder2, filename):
  """
  Compares columns and rows between two CSV files with the same filename.

  Args:
      folder1: Path to the first folder (CityA).
      folder2: Path to the second folder (CityB).
      filename: Name of the CSV files to compare.

  Returns:
      A dictionary containing information about column and row mismatches.
  """

  mismatches = {}

  # Get full paths to the CSV files
  file1_path = os.path.join(folder1, filename)
  file2_path = os.path.join(folder2, filename)

  try:
    # Read CSV files using pandas
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Check if column names are identical
    if not df1.columns.tolist() == df2.columns.tolist():
      mismatches["column_names"] = "Column names differ between files."
      return mismatches  # Early exit for different column names

    # Compare rows for columns with the same name
    for col in df1.columns:
      if col in df2:
        # Check if number of rows is the same
        if len(df1[col]) != len(df2[col]):
          mismatches[col] = "Different number of rows in column."
        else:
          # Compare corresponding row values (excluding potential NaN values)
          mismatched_rows = (df1[col] != df2[col]).dropna().index.tolist()
          if mismatched_rows:
            mismatches[col] = f"Values differ at rows: {mismatched_rows}"

  except FileNotFoundError:
    mismatches["error"] = f"File not found: {filename}"

  return mismatches

# Example usage
folder1 = "20231231"
folder2 = "20240331"
filename = "L2_LOAN_DEPOSIT.csv"

mismatches = compare_csv_files(folder1, folder2, filename)

if mismatches:
  print(f"File '{filename}':")
  for key, value in mismatches.items():
    print(f"\t- {key}: {value}")
else:
  print(f"Files '{filename}' appear to be identical.")
'''