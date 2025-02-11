import os

# 1. Set the folder path containing the files you want to rename
FOLDER_PATH = r"/path/to/your/folder"

# 2. Define the base name you want to use
BASE_NAME = "newname"

def main():
    # Get a list of all files (not directories) in the specified folder
    files = [f for f in os.listdir(FOLDER_PATH) 
             if os.path.isfile(os.path.join(FOLDER_PATH, f))]

    # Optional: Sort the files so renaming happens in alphabetical order
    files.sort()

    # 3. Rename each file with an incrementing number
    counter = 1
    for old_filename in files:
        # Extract the file extension
        _, extension = os.path.splitext(old_filename)

        # Construct the new filename using zero-padded numbers (e.g., 0001, 0002, ...)
        new_filename = f"{BASE_NAME}_{counter:04d}{extension}"
        
        old_path = os.path.join(FOLDER_PATH, old_filename)
        new_path = os.path.join(FOLDER_PATH, new_filename)

        # Rename the file
        os.rename(old_path, new_path)

        print(f"Renamed: {old_filename} -> {new_filename}")
        counter += 1

if __name__ == "__main__":
    main()
