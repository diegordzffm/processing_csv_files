import zipfile
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

    # Clean up extracted files
    import shutil
    shutil.rmtree(extract_dir1)
    shutil.rmtree(extract_dir2)

    return same_count, different_count, compared_files

# Paths to the zip files
zip_path1 = 'ingestion_CKV_Test_20240131_lot01.zip'
zip_path2 = 'ticket_291599_ingestion_CKV_GDM_20231231_lot15.zip'

# Compare the contents
same_count, different_count, compared_files = compare_zip_contents(zip_path1, zip_path2)

print(f'Same files: {same_count}')
print(f'Different files: {different_count}')
print(f'Compared files: {compared_files}')
