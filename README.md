### Django rest framework app to manage mailboxes

#### Technologies:
Project is created with:
* PostgreSQL
* Python 3.8
* Celery
* Redis
* Django Rest Framework


#### Setup step by step:
* git-clone https://github.com/Mefpef/mailapi.git
* source env/bin/activate
* pip install -r requirements.txt
* cd mailAPI
* python3 manage.py makemigrations
* python3 manage.py migrate
* python3 manage.py runserver


```commandline
$ REMEMBER TO CREATE .ENV FILE IN mailAPI folder with you postgreSQL db configuration!
```