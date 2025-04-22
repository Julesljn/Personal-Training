import os

# os.listdir(path) → Lists the contents of a directory (files + folders)
# os.path.isfile(path) → Checks if a path is a file
# os.path.isdir(path) → Checks if a path is a directory
# os.path.getsize(path) → Returns the size of a file in bytes
# os.path.abspath(path) → Gets the absolute path of a file or folder
# os.path.join(path1, path2, ...) → Joins path components safely (cross-platform)
# os.path.getmtime(path) → Returns the last modification time (timestamp)

def listAndDetails(path):
    lines = []
    for element in os.listdir(path): 
        uniquePath = os.path.join(os.path.abspath(path), element)
        sizePath = os.path.getsize(uniquePath)
        if os.path.isfile(uniquePath):
            lines.append(f'{element} --> \033[91mFichier\033[0m -> {sizePath}')
        else:
            lines.append(f'{element} --> \033[92mDossier\033[0m -> {sizePath}')

    return '\n'.join(lines)

print(listAndDetails('../../..'))