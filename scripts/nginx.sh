#!/usr/bin/bash

sudo systemctl daemon-reload
systemctl restart gunicorn.service
sudo cp /nginx/nginx.conf /etc/nginx/sites-available/django-movieApp
sudo ln -s /etc/nginx/sites-available/django-movieApp/etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'