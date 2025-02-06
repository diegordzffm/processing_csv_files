import os

def remove_suffix(folder_path):
    """
  This function removes the suffix of all CSV files in a specified folder.

  Args:
      folder_path (str): The path to the folder containing CSV files.
    """
    for filename in os.listdir(folder_path):
        print("filename is")

folder_path = "20231231"  # Replace with the actual folder path

'''

 for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
      base_name, _ = os.path.splitext(filename)  # Separate base name and extension
      new_filename = os.path.join(folder_path, base_name)  # Construct new filename
      os.rename(os.path.join(folder_path, filename), new_filename)  # Rename the file

# Example usage
folder_path = "your/folder/path"  # Replace with the actual folder path
remove_csv_suffix(folder_path)
print("CSV file suffixes removed successfully!")

'''