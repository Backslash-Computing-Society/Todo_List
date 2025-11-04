import os

# 🔧 Set the directory path
folder_path = input("Enter the folder path: ")

# Check if path exists
if not os.path.exists(folder_path):
    print("❌ Folder not found!")
else:
    # List all files in the folder
    files = os.listdir(folder_path)
    print(f"Found {len(files)} files.")

    # Example: rename all files with new naming pattern
    for count, filename in enumerate(files, start=1):
        file_ext = os.path.splitext(filename)[1]  # get file extension
        new_name = f"file_{count}{file_ext}"      # rename pattern
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)

        os.rename(src, dst)

    print("✅ All files renamed successfully!")
