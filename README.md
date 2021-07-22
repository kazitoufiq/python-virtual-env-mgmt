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


## using virtualenvwrapper-win

pip install virtualenvwrapper-win

### To create a virtual env in a centralized directory
mkvirtualenv <venv_name>           
 
### To list all the available virtual env created using virtualenvwrapper-win in the system    
workon
  
deactivate

### To activate an environment  
workon <venv_name>
  

