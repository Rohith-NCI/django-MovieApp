#!/usr/bin/bash 

sed -i 's/\[]/\["3.84.7.210"]/' /home/ubuntu/django-movieApp/movieApp/settings.py
sudo systemctl restart gunicorn
sudo systemctl restart nginx
