import os
import shutil

fileExts = set()
files = [f for f in os.listdir('.') if os.path.isfile(f)]

for f in files:
    print(f)
    fileExts.add(f.split(".")[-1])

for ext in fileExts:
    try:
        os.mkdir(ext.capitalize())
    except Exception as e:
        print(e)

if __file__ in files:
    files.remove(__file__)

for f in files:
    try:
        shutil.move(f,f.split(".")[-1].capitalize())
    except Exception as e:
        print(e)
