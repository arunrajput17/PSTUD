## Packages

#What are packages?
#Published collection of modules

#How do i find packages?
# URL Python package index
# internet search

####### Installing packages

# install an individual package
pip install colorama

# install from a list of packages
pip install -r requirements.txt

# requirements.txt
colorama


##### Virtual environments

#By default, packages are installed globally
# --> version management becomes a challenge

# Virtual environments can be used to contain and manage package of collections
#--> Really just a folder behind the scenes with all the packages


### Creating virtual environments

# install viirtual environment
pip install virtualenv

# Windows system
python -m venv <folder_name>

# OSX / Linux (bash)
virtualenv <folder_name>

### Using virtual environments

# Windows system
# cmd.exe
<folder_name>\Scripts\Activate.bat

# Powershell
<folder_name>\Scripts\Activate.ps1

# Bash shell
../<folder_name>\Scripts\Activate

# OSX / Linux (bash)
<folder_name>\bin\Activate


### Installing packages in virtual environment

# install an individual package
pip install colorama

# install from a list of packages
pip install -r requirements.txt

# requirements.txt
colorama

