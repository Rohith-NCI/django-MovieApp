# # #!/usr/bin/bash

# # echo "Pull Finished"
# # sudo systemctl daemon-reload
# # sudo systemctl restart nginx

# #!/usr/bin/env bash

# # kill any servers that may be running in the background 
# sudo pkill -f runserver


# # kill frontend servers if you are deploying any frontend
# # sudo pkill -f tailwind
# # sudo pkill -f node

# cd /home/ubuntu/django-movieApp/

# # activate virtual environment
# python3 -m venv venv
# source venv/bin/activate

# install requirements.txt
# pip install -r /home/ubuntu/django-movieApp/requirements.txt

# # run server
# screen -d -m python3 manage.py runserver 0:8080

#!/usr/bin/env bash

# kill any servers that may be running in the background 
sudo pkill -f runserver

# kill frontend servers if you are deploying any frontend
# sudo pkill -f tailwind
# sudo pkill -f node

# cd /home/ubuntu/django-movieApp/

# activate virtual environment
python3 -m venv /home/ubuntu/django-movieApp/venv
source /home/ubuntu/django-movieApp/venv/bin/activate

#install /home/ubuntu/django-movieApp/requirements.txt
pip install django
python -m pip install Pillow
pip install -r /home/ubuntu/django-movieApp/requirements.txt

# firewall-cmd --zone=public --permanent --add-port=8080/tcp

# firewall-cmd --reload

sudo firewall-cmd --zone=public --permanent --add-port=8080/tcp sudo firewall-cmd --reload

# sudo firewall-cmd --zone=public --permanent ----add-service=mysql sudo firewall-cmd --reload

# run server
screen -d -m python3 /home/ubuntu/django-movieApp/manage.py runserver 0:8080
