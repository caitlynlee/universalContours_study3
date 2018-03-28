import os
import shutil


cwd = os.getcwd()

for subName in os.listdir(cwd):

    subDir = os.path.join(cwd, subName)

    if os.path.isdir(subDir):
        for f in os.listdir(subDir):
            if len(f.split(".")) == 2:
                if (f.split("_")[1] != "walk"):
                    os.remove(os.path.join(subDir, f))
                    continue

                if (f.split(".")[1] == "ptd"):
                    src = os.path.join(subDir, f)
                    dst = os.path.join(subDir, f.split(".")[0] + ".txt")

                    os.rename(src, dst)
