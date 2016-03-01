import glob
import os

files = glob.glob("*cycle*.log")
files.sort(key=os.path.getmtime)
print("\n".join(files))
