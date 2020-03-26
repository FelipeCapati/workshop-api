# COGNITIVE LIGHTHOUSE: WORKSHOP API EXAMPLE #
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Abstract ##
Validates if the number is greater than or less than 10 and shows whether the boolean was True or False.

## I. Development Requirements ##

### A. Versions ###
 - Python [3.7.4](https://www.python.org/downloads/release/python-374/)

### B. Running Server ###
```bash
$ pip3 install -r requirements.txt
$ python3 .
```

### C. Running Tests ###
```bash
$ pip3 install -r requirements.txt
$ pytest
```

### D. Save requirements.txt ###
```bash
pip freeze > requirements.txt
```

### E. Build doc ###
```bash
apidoc -i src/ -o doc/
```

### F. Command to build project in docker ###
```bash
sudo docker build -t kpmg-workshop-api .
sudo docker run -p 9000:9000 -d kpmg-workshop-api
```

## II. Deployment Requirements ##

### A. Environment Variables ###
 We created a class named `EnvironmentVariable` in the path `src/infra/utility/environment` of the project and added the 
 following values in method to change a default values:
 
| Variables | Description | Accepeted Values |
|-----------|-------------|-----------------|
| get_system_port | Port where the app will start | Any number |
| get_system_debug | Flask debug option  | True or False |
| get_basic_auth_user | Basic Auth default user | Any string |
| get_basic_auth_password | Basic Auth default password | Any string |
| get_upload_folder | Default path temp  | any string |

## IV. Todo ##
 - Implement more feature to system

## V. License ##
Private Software
_______________________________________________________
