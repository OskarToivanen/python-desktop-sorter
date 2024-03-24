import os
import shutil
from datetime import datetime

# Get the current user desktop path.
if os.name == 'nt':  # Windows
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
else:  # macOS and Linux
    desktop_path = os.path.join(os.environ['HOME'], 'Desktop')

dest_folder_path = 'Folderbank'
dest_path = os.path.join(desktop_path, dest_folder_path) # Uses os.path.join to create a full path for destination folder.

# File destination folder dictionary.
file_type_mapping = {
 '.pdf': 'PDFs',
 '.doc': 'Documents', '.docx': 'Documents', '.txt': 'Documents',
 '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
 '.exe': 'Apps', '.msi': 'Apps',
}

# Check if the dest_path exist.
if not os.path.exists(dest_path):
 os.makedirs(dest_path)

files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]

for file in files:
 # Create file_path for current file. 
 file_path = os.path.join(desktop_path, file)

 # Find out files extension.
 file_extension = os.path.splitext(file)[1].lower()
 file_category = file_type_mapping.get(file_extension, 'Other') # If not found default to 'Other'.

 # Use datetime to get last modified time by modifying the os.getmtime.
 modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))
 month_folder_name = modification_time.strftime('%Y-%m') # Create folder name for monthly sorting.

 # Build directory path for sorting.
 dest_dir_path = os.path.join(dest_path, file_category, month_folder_name) # ex. C:\\Users\\Oskar\\Desktop\\Folderbank\\Pdfs\\2023-01

 # Create sorter dir path if does not exist.
 if not os.path.exists(dest_dir_path):
    os.makedirs(dest_dir_path)    

 # Move the file to the correct directory using shutil.move().
 shutil.move(file_path, dest_dir_path)
 print(f"Moved: '{file}' to '{os.path.join(file_category, month_folder_name)}'")
    
print('All files have been sorted successfully.')