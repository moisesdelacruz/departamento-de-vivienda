#!/bin/bash

set -e

# set Environment Variables
source .env
# activate environment virtual
virtualenv .vivienda
source .vivienda/bin/activate

# run command
python manage.py __createsuperuser
