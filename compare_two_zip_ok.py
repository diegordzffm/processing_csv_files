'''import zipfile
import pandas as pd
import os
import filecmp


def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def get_csv_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]

def compare_csv_files(file1, file2):
    # Load CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Compare dataframes
    return df1.equals(df2)

def compare_zip_contents(zip_path1, zip_path2):
    extract_dir1 = "extract1"
    extract_dir2 = "extract2"

# Extract both zip files
    extract_zip(zip_path1, extract_dir1)
    extract_zip(zip_path2, extract_dir2)
    
    # Get lists of CSV files
    csv_files1 = get_csv_files(extract_dir1)
    csv_files2 = get_csv_files(extract_dir2)

# Compare files
    same_count = 0
    different_count = 0
    compared_files = []

    for file1 in csv_files1:
        file1_name = os.path.basename(file1)
        for file2 in csv_files2:
            file2_name = os.path.basename(file2)
            if file1_name == file2_name:
                if compare_csv_files(file1, file2):
                    same_count += 1
                else:
                    different_count += 1
                compared_files.append(file1_name)
                break



# Paths to the zip files
zip_path1 = 'ingestion_CKV_Test_20240131_lot01.zip'
zip_path2 = 'ticket_291599_ingestion_CKV_GDM_20231231_lot15.zip'

# Compare the contents
#same_count, different_count, compared_files = compare_zip_contents(zip_path1, zip_path2)'''




import zipfile
from collections import Counter

def compare_zip_csvs(zip_folder1, zip_folder2):
  """
  Compares CSV files within two zip folders and returns counts of same and different files.

  Args:
    zip_folder1: Path to the first zip folder.
    zip_folder2: Path to the second zip folder.

  Returns:
    A dictionary with keys 'same' and 'different' containing counts of matching and mismatched filenames.
  """
  file_counts = Counter()
  with zipfile.ZipFile(zip_folder1, 'r') as zip1, zipfile.ZipFile(zip_folder2, 'r') as zip2:
    for info1 in zip1.infolist():
      if not info1.filename.endswith('.csv'):
        continue
      filename = info1.filename
      # Check if file exists in both zips
      if filename in [info.filename for info in zip2.infolist()]:
        with zip1.open(filename) as f1, zip2.open(filename) as f2:
          # Basic check for content similarity (you can use libraries like pandas for deeper comparison)
          if f1.read() == f2.read():
            file_counts['same'] += 1
          else:
            file_counts['different'] += 1
      else:
        file_counts['different'] += 1
  return file_counts

# Example usage (replace paths with your actual zip folders)
zip_folder1 = "ticket_291599_ingestion_CKV_GDM_20231231_lot15.zip"
zip_folder2 = "ticket#291599_ingestion_CKV_GDM_20240331_lot07.zip"
results = compare_zip_csvs(zip_folder1, zip_folder2)

print(f"Same files: {results['same']}")
print(f"Different files: {results['different']}")

