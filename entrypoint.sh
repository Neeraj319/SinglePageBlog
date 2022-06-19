#!/bin/bash

while !</dev/tcp/db/5432; do sleep 1; done;
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8000