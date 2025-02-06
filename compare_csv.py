import pandas as pd
import csv

def compare_csv_files(file1, file2):
    # Read CSV files
    # Open CSV files
  with open(file1, 'r') as csvfile1, open(file2, 'r') as csvfile2:
    reader1 = csv.reader(csvfile1)
    reader2 = csv.reader(csvfile2)
    
    # Get headers
    headers1 = next(reader1)
    headers2 = next(reader2)

    # Find common columns
    common_columns = [col for col in headers1 if col in headers2]


    # Iterate through rows
    for row1 in reader1:
      for row2 in reader2:
        for col in common_columns:
          # Check if values exist in both columns (at least once)
          if row1[headers1.index(col)] != row2[headers2.index(col)]:
            # Values differ, skip to next row in file2
            break
        else:
          # All values in common columns match for this pair of rows
          print(f"Match found: Row {reader1.line_num} in {file1} matches Row {reader2.line_num} in {file2}")
          break  # No need to check further for this row1

    

if __name__ == "__main__":
  file1 = "AnaCounterparty_RMM_AGID6305574_adjusted_newformat2.csv"  # Replace with your actual file path
  file2 = "AnaCounterparty_RMM_AGID6305574.csv"  # Replace with your actual file path

# File names
#file1 = "AnaCounterparty_RMM_AGID6305574_adjusted_newformat2.csv"
#file2 = "AnaCounterparty_RMM_AGID6305574.csv"

compare_csv_files(file1, file2)
