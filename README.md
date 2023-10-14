# python-virtual-env-mgmt


## Using virtualenvwrapper-win

pip install virtualenvwrapper-win

### To create a virtual env in a centralized directory
mkvirtualenv <venv_name>           
 
### To list all the available virtual envs created using virtualenvwrapper-win in the system    
workon

### To deactivate
deactivate

### To activate an environment  
workon <venv_name>
  



### Use VIRTUAL ENV with Jupyter notebook within VS CODE

1) Press Command+Shift+P to open a new command pallete

2) Type >Python: Select Intepreter to start jupyter notebook server

3) Open the notebook again


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


### To create env with speccific python version


C:/Users/{username}/AppData/Local/Programs/Python/Python39/python.exe -m venv llm_env
