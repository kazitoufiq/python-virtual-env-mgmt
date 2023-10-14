### To check all the available python version

import os
import glob

# Typical paths for Python installations


paths = [
    r"C:\Python*",
    r"C:\Users\{}\AppData\Local\Programs\Python\Python*".format(os.getlogin())
]


for path in paths:
    for python_path in glob.glob(path):
        os.system('{}\python.exe --version'.format(python_path))
