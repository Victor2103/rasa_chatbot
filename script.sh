#!/bin/sh
# Shell script to open terminals
# and execute a separate command in each

#The gnome terminal command doesn't work in a dockerfile because we can't open terminal.
#gnome-terminal -- bash -c "cd rasa_bot && rasa run -m models --enable-api --cors '*'"
#gnome-terminal -- bash -c "cd django_app && python3 manage.py runserver"

cd rasa_bot && rasa run -m models --enable-api --cors '*' &
cd django_app && ls && python3 manage.py runserver 0.0.0.0:8000
