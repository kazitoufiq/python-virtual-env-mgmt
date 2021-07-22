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
mkvirtualenv <env-name>             //will create a virtual env in a centralized directory
  
workon // to list all the available virtual env created using virtualenvwrapper-win in the system   
  
deactivate
  
workon <env-name>   //to activate a environment     
  

