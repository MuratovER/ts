# ts
Creating project gaimification on django

## pushing

git status 

git add -A .  
git status  

git commit -m 'comment'

git push -u origin 'branch'    
_______________________________________________________________________________________________________________

## virtual environment
venv


## pip

Django
django-extensions
psycopg2
dj-database-url
gunicorn 
whitenoise




## migrations

python manage.py makemigrations "module"

python manage.py migrate "module"

## PostgreSQL installation

###here you need to download PostgreSQL

http://www.enterprisedb.com/products-services-training/pgdownload#windows

### Instruction for installing

http://www.postgresqltutorial.com/install-postgresql/

### Creating the database

(venv) C:\ts> psql
###Our > now changed into #, which means that we're now sending commands to PostgreSQL. Let's create a user with CREATE USER name;

_______________________________________________________________________________________________________________

## (remember to use the semicolon)

:# CREATE USER name;

:# CREATE DATABASE ts OWNER name;

### after this you need to download psycopg2.exe

pip install psycopg2

### after installing we need to applay migrations 

### and at the end we need to create superuser

python manage.py createsuperuser --username name

_______________________________________________________________________________________________________________

## or you can use SQL shell

![SQL Shell](https://ibb.co/Qp9cQXn)

### and repeat all steps
:# CREATE USER name;

:# CREATE DATABASE ts OWNER name;

### after this you need to download psycopg2.exe

pip install psycopg2

### after installing we need to applay migrations 

### and at the end we need to create superuser

python manage.py createsuperuser --username name

_______________________________________________________________________________________________________________

## requirements.txt

(venv) C:\ts> pip install dj-database-url gunicorn whitenoise

(venv) C:\ts> pip freeze > requirements.txt

### Open this file and add the following line at the bottom:

psycopg2==2.7.2
