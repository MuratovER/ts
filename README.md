




# pushing

git status 

git add -A .  

git status  

git commit -m 'comment'

git push -u origin 'branch'    
_______________________________________________________________________________________________________________
#How to add new branch

git branch <branch name>

git checkout <branch name> 
# virtual environment

venv

#### установка
python -m venv myvenv

#### запуск
C:\ts venv\scripts\sctivate

(venv) C:\ts>

_______________________________________________________________________________________________________________

# pip

Django
django-extensions
psycopg2
dj-database-url
gunicorn 
whitenoise



_______________________________________________________________________________________________________________

# migrations

python manage.py makemigrations "module"

python manage.py migrate "module"

# PostgreSQL installation

#### here you need to download PostgreSQL

http://www.enterprisedb.com/products-services-training/pgdownload#windows

#### Instruction for installing

http://www.postgresqltutorial.com/install-postgresql/

_______________________________________________________________________________________________________________


# Creating the database

(venv) C:\ts> psql
#### Our > now changed into #, which means that we're now sending commands to PostgreSQL. Let's create a user with CREATE USER name;


### (remember to use the semicolon)

:# CREATE USER name;

:# CREATE DATABASE ts OWNER name;

### after this you need to download psycopg2.exe

pip install psycopg2

### after installing we need to applay migrations 

python manage.py migrate "module"

### and at the end we need to create superuser

python manage.py createsuperuser --username name


## Or you can use SQL shell and repeat al steps with them


_______________________________________________________________________________________________________________

# requirements.txt

(venv) C:\ts> pip install dj-database-url gunicorn whitenoise

(venv) C:\ts> pip freeze > requirements.txt

## Open this file and add the following line at the bottom:

psycopg2==2.7.2


# Procfile 

web: gunicorn mysite.wsgi --log-file -

# runtime.txt

python-3.6.4

# mysite/wsgi.py
Open the mysite/wsgi.py file and add these lines at the end:

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)


# deploy on HEROKU

(venv) C:\ts>heroku create djangogirlsblog

(venv) C:\ts>git push heroku master

(venv) C:\ts>heroku ps:scale web=1

(venv) C:\ts>heroku open

(venv) C:\ts>heroku run python manage.py migrate

(venv) C:\ts>heroku run python manage.py createsuperuser