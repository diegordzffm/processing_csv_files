import pandas as pd

def compare_csv_files(file1, file2):
    # Read CSV files with improved error handling
    df1 = pd.read_csv(file1, delimiter=',', encoding='utf-8', on_bad_lines='skip', engine='python')
    df2 = pd.read_csv(file2, delimiter=',', encoding='utf-8', on_bad_lines='skip', engine='python')
    
    # Compare column names
    columns1 = set(df1.columns)
    columns2 = set(df2.columns)
    
    missing_in_df2 = columns1 - columns2
    missing_in_df1 = columns2 - columns1
    
    print("Columns in file1 but not in file2:", missing_in_df2)
    print("Columns in file2 but not in file1:", missing_in_df1)
    
    # Get common columns
    common_columns = columns1.intersection(columns2)
    
    # Compare values row-wise for common columns
    differences = []
    for col in common_columns:
        if df1.shape[0] == df2.shape[0]:  # Ensure both have the same number of rows
            diff_rows = df1[col] != df2[col]
            if diff_rows.any():
                differences.append((col, df1.loc[diff_rows, col], df2.loc[diff_rows, col]))
    
    # Display differences
    for col, df1_values, df2_values in differences:
        print(f"Differences in column: {col}")
        print("File1 values:")
        print(df1_values)
        print("File2 values:")
        print(df2_values)
        print("="*50)

# File names
file1 = "AnaCounterparty_RMM_AGID6305574_adjusted_newformat2.csv"
file2 = "AnaCounterparty_RMM_AGID6305574.csv"

compare_csv_files(file1, file2)
