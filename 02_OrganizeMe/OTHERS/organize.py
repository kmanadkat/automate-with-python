import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'OTHERS'

def organizeDirectory():
    for item in os.scandir():
        # If found Directory then skip
        if item.is_dir():
            continue

        # Get File Extension
        filePath = Path(item)
        fileType = filePath.suffix.lower()

        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        # Create Directory If Not Exists
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        
        # Move File
        filePath.rename(directoryPath.joinpath(filePath))


organizeDirectory()