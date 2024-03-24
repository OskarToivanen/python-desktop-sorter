import os
import shutil
from datetime import datetime

desktop_path = 'C:\\Users\\Oskar\\Desktop'
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

 