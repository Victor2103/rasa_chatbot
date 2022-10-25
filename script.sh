#!/bin/sh
# Shell script to open terminals
# and execute a separate command in each

gnome-terminal -- bash -c "cd rasa_bot && rasa run -m models --enable-api --cors '*'"
gnome-terminal -- bash -c "cd django_app && python3 manage.py runserver"

