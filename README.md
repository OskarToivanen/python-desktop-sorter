# Desktop File Organizer
I created this organizer to manage my cluttered desktop. The script designed to help users automatically sort files on their desktop into categorized folders based on file type and the date of last modification.

## Features

**Automatic Sorting**: Files are moved from the desktop to the Folderbank directory, where they are organized into subfolders by file type (e.g., PDFs, Documents, Images, Apps).

**Monthly Organization**: Within each file type folder, files are further sorted into subfolders named after the month of the file's last modification date, allowing for easy tracking of files over time.

**Dynamic Folder Creation**: The script dynamically creates necessary directories if they do not exist, ensuring a smooth sorting process without manual folder setup.

**Customizable File Types**: Users can easily modify the file_type_mapping dictionary within the script to support additional file types and corresponding destination folders.

# Setup and Usage
1. **Download the Script**: Clone or download the DesktopFileOrganizer.py script to your local machine.
   
2. **Customize File Types (Optional)**: Open the script in a text editor or IDE and modify the file_type_mapping dictionary if you want to add or change the file type categorization.
   
3. **Run the Script**:
    * Open a terminal or command prompt.
    * Navigate to the directory containing the script.
    * Run the script with Python by executing python DesktopFileOrganizer.py.
      
4. **Check the Results**: After running, check the Folderbank directory on your desktop for the organized files.
