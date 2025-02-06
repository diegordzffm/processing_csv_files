import os

def add_suffix_to_csv(folder_path, suffix):
  """
  Adds a suffix to the names of all CSV files in a folder.

  Args:
    folder_path (str): Path to the folder containing CSV files.
    suffix (str): Suffix to be added to the filenames (e.g., "_modified").
  """

  # Get all files in the folder
  for filename in os.listdir(folder_path):
    # Check if it's a CSV file
    if filename.endswith(".csv"):
      # Split filename and extension
      file_base, file_ext = os.path.splitext(filename)

      # Create new filename with suffix
      new_filename = f"{file_base}{suffix}{file_ext}"

      # Construct full paths
      old_path = os.path.join(folder_path, filename)
      new_path = os.path.join(folder_path, new_filename)

      # Rename the file
      os.rename(old_path, new_path)
      print(f"Renamed: {filename} to {new_filename}")

if __name__ == "__main__":
  folder_path = "folder_20231231"  # Replace with your actual folder path
  suffix = ""  # Suffix to add (e.g., "_processed")
  add_suffix_to_csv(folder_path, suffix)
