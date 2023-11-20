import os
os.makedirs('/path/to/your/new/folder', exist_ok=True)
import os
folder_path = '/path/to/your/new/folder'
files = os.listdir(folder_path)
for file in files:
    print(file)
