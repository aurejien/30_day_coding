import os
import shutil

chemin = "dossier_source/"
liste = os.listdir(chemin)

extender = ["musiques", "images", "videos", "textes"]

for i in extender:
    os.mkdir(chemin + i)

for i in liste:
    extention = i[-3:]
    source =  chemin + i

    if extention == "mp3" or extention == "wav":
        folder = chemin + "/musiques"
        shutil.move(source, folder)
    elif extention == "png" or extention == "peg" or extention == "jpg":
        folder = chemin + "/images"
        shutil.move(source, folder)
    elif extention == "mov" or extention == "mp4":
        folder = chemin + "/videos"
        shutil.move(source, folder)
    elif extention == "pdf":
        folder = chemin + "/textes"
        shutil.move(source, folder)