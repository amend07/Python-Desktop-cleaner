import os
import shutil

desktop = os.path.expanduser("~/Desktop")
list_files = os.listdir(desktop)
print(list)
full_path = os.path.join(desktop, "desktop.ini")
print(full_path)

# create a dictionary to store files with their expansions
files_by_extensions = {}
# loop all files in desktop
for files in list_files:
    file_paths = os.path.join(desktop, files)
    # check if it's a file
    if os.path.isfile(file_paths):
        file_extension = os.path.splitext(files)[1]
        # add file extension in dictionary
        if file_extension not in files_by_extensions:
            files_by_extensions[file_extension] = []

        files_by_extensions[file_extension].append(file_paths)
        # create a folder for each extension
for file_extension,file_paths in files_by_extensions.items():
    folder = f"{file_extension[1:].upper()} files"
    folder_path = os.path.join(desktop, folder)

    # create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # moving the files to created folder
    for file_path in file_paths:
        shutil.move(file_path, folder_path)

