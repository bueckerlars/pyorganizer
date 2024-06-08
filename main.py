import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Downloads")

extensions = {
    ".jpg": "Bilder",
    ".png": "Bilder",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".docx": "Dokumente",
    ".pdf": "Dokumente",
    ".txt": "Dokumente",
    ".mp3": "Musik",
    ".wav": "Musik"
}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension]

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extension")
    else:
        print(f"Skipped {filename}. It is a directory.")

print("File organizer completed.")