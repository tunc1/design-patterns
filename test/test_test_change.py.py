import os
from pathlib import Path

path=str(Path(__file__).resolve().parent)
print(path)
files=os.listdir(path)
for file in files:
    name=(file.split("_test.py"))
    os.rename(path+"\\"+file,path+"\\test_"+name[0])