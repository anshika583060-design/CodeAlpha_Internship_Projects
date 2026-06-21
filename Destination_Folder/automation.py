import os
import shutil

# destination folder ka path (apne computer ke hisaab se)
destination = 'C:/Users/anshi/OneDrive/Desktop/Destination_Folder'

# Agar folder nahi hai, toh bana do
if not os.path.exists(destination):
    os.makedirs(destination)

# .jpg files ko move karo
for file in os.listdir('.'):
    if file.endswith('.jpg'):
        shutil.move(file, os.path.join(destination, file))
        print(f"Moved: {file}")

print("Done! Files moved.")