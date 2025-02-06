from zipfile import ZipFile
from collections import defaultdict

def count_csv_rows_in_zips(zip_folder1, zip_folder2):
  """
  This function counts the number of rows in CSV files with the same name
  present in two different zip folders.

  Args:
      zip_folder1: Path to the first zip folder (string).
      zip_folder2: Path to the second zip folder (string).

  Returns:
      A dictionary where keys are CSV file names (strings) and values are
      lists containing the number of rows in each corresponding file
      found in the zip folders (integers).
  """
  row_counts = defaultdict(list)
  with ZipFile(zip_folder1, 'r') as zip1, ZipFile(zip_folder2, 'r') as zip2:
    for filename in zip1.namelist():
      if filename.endswith('.csv'):
        with zip1.open(filename) as f1, zip2.open(filename) as f2:
          # Count rows efficiently using generator expression
          row_counts[filename].append(sum(1 for _ in f1))
          row_counts[filename].append(sum(1 for _ in f2))

  return row_counts

# Example usage
zip_folder1 = "ingestion_CKV_Test_20240131_lot01.zip"
zip_folder2 = "ticket_291599_ingestion_CKV_GDM_20231231_lot15.zip"
row_counts = count_csv_rows_in_zips(zip_folder1, zip_folder2)

# Print results
for filename, counts in row_counts.items():
  print(f"File: {filename}")
  for i, count in enumerate(counts):
    print(f"\tZip folder {i+1}: {count} rows")

