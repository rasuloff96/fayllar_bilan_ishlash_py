import os
import platform
import json
import shutil
import subprocess
from datetime import datetime


# Papka yaratish uchun os modulidan foydalanildi.

folder_name = "chiquvchi_fayllar"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"{folder_name} nomli papka yaratildi.")
else:
    print(f"{folder_name} nomli papka allaqachon mavjud.")

file_path = os.path.join(folder_name, "malumotlar.txt")

files = os.listdir(folder_name)
print("Papkadagi fayllar:" , files)



with open(pcs.json, "r") as file:
    all_pcs = json.load(file)
    
    