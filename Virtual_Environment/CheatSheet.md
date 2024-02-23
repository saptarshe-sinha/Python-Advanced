# Python virtual environment CheatSheet

## Install virtualend
`pip install virtualenv`

## Create a new virtual environment
`python -m venv env_name`

## In Windows, activate the new python environment
`.\env_name\Scripts\activate`

## In Linux or Mac, activate the new python environment
`source env_name/bin/activate`

## Install packages
`pip install package_name`

## Save installed packages to a file
`pip freeze > requirements.txt`
or 
`pip list --format=freeze > requirements.txt`

## Install packages from a file
`pip install -r requirements.txt`

## Deactivate the current virtual environment
`deactivate`



