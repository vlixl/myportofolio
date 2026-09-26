#!/bin/bash

# To initialize the website, open the terminal and type:
# ./init.sh
python manage.py shell < data/all_data.py

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=vlixl-tech@gmail.com
export DJANGO_SUPERUSER_PASSWORD=secret-password

python manage.py createsuperuser --noinput

