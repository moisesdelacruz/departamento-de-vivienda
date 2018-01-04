#!/bin/bash

set -e

# get data for build
while [[ $DB_NAME == '' ]]
do
  read -p "Type db name: " DB_NAME
done

while [[ $DB_USER == '' ]]
do
  read -p "Type db user: " DB_USER
done

while [[ $DB_PASS == '' ]]
do
  read -p "Type db pass: " DB_PASS
done

while [[ $DB_HOST == '' ]]
do
  read -p "Type db host: " DB_HOST
done

# Installing python-pip, libpq-dev, python-dev
echo "Installing python-pip, libpq-dev, python-dev ..."
sudo apt-get update
sudo apt-get install python-pip libpq-dev python-dev

# install postgresql
echo "Installing postgresql..."
sudo apt-get install postgresql postgresql-contrib

# Create Database
echo "Creating Database"
sudo -u postgres psql <<END_OF_SQL
CREATE DATABASE $DB_NAME;
CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
END_OF_SQL

# Installing virtualenv
echo "Installing virtualenv"
sudo -H pip install --upgrade pip
sudo -H pip install virtualenv

virtualenv .vivienda
source .vivienda/bin/activate

pip install -r requirements.txt

# Set environment variables
echo "Creating .env file"

cat <<EOF >.env
export DB_NAME=$DB_NAME
export DB_USER=$DB_USER
export DB_PASS=$DB_PASS
export DB_HOST=$DB_HOST
EOF

echo "build completed..."
echo "exiting..."
echo "for create superuser execute: 'python manage.py createsuperuser'"
echo "for run project execute: 'python manage.py run'"
