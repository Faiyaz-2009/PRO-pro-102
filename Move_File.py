import shutil 
import os

fromdir = "C:/Users/faiya/Downloads"
todir = "C:/Python of Byjus/Projects of PRO"
listoffiles = os.listdir(fromdir)
print(listoffiles)

for filename in listoffiles:
    name, ext = os.path.splitext(filename)

    if(ext == ""):
        continue
    if ext in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = fromdir + "/" + filename
        path2 = todir + "/" + "Download_files"
        path3 = todir + "/" + "Download_files" + "/" + filename
        print("source ", path1)
        print("destination ", path3)
        if os.path.exists(path2):
            print("Moving" + filename + "......")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving" + filename + "......")
            shutil.move(path1, path3)