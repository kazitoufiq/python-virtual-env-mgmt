# python-virtual-env-mgmt

cd ~
mkdir .virtualenvs

cd .virtualenvs

pip install virtualenv  #if not installed

virtualenv --version

virtualenv <venv_name>

## Windows

<venv_name>\Scripts\activate

## Linux/Mac OS

source <venv_name>/bin/activate


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



