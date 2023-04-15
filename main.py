import os
import shutil

#Organiza los archivos de una carpeta , en carpetas creadas por tipo de archivo

path = input("Enter path:")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension=extension[1:]
    if os.path.exists(path + "/" + extension):
        shutil.move(path + "/" + file, path + "/" + extension + "/" + file)
    else:
        os.makedirs(path + "/" + extension)
        shutil.move(path+"/"+ file, path + "/" + extension)