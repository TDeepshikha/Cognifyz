import os
import shutil
source_directory = 'path/to/your/directory'
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.ogg'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Archives': ['.zip', '.tar', '.gz'],
}
def organize_files(directory):
    for folder_name, extensions in file_types.items():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            continue
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(os.path.join(directory, filename), os.path.join(directory, folder_name, filename))
                moved = True
                print(f'Moved: {filename} -> {folder_name}/')
                break
        if not moved:
            print(f'File type not recognized, leaving: {filename}')
if __name__ == '__main__':
    organize_files(source_directory)
