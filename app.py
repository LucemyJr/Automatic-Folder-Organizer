import os
from tkinter.filedialog import askdirectory

pathFolder = askdirectory(title="Selecione uma pasta")

fileList = os.listdir(pathFolder)

local = {
    "Imagens": [".png", ".jpeg", ".jpg", ".webp"],
    "Compactados": [".zip"],
    "Pdfs": [".pdf", ".pptx"],
    "Design": [".cdr", ".ttf"],
    "Executaveis": [".exe", ".msi"],
}

for files in fileList:
    name, extension = os.path.splitext(f"{pathFolder}/{files}")
    for folder in local:
        if extension in local[folder]:
            if not os.path.exists(f"{pathFolder}/{folder}"):
                os.mkdir(f"{pathFolder}/{folder}")
            os.rename(f"{pathFolder}/{files}", f"{pathFolder}/{folder}/{files}")