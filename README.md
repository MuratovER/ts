

## Требования для начала работы с проектом

- Python 3, pip, Visual Studio Code
- Аккаунт Github
- Скинуть Эльдару почту от аккаунта GitHub для добавление в контрибуторов проекта

## Начало работы с проектом

Команды для для локальной установки среды разработки:

### Клонирования проекта

git clone https://github.com/MuratovER/ts.git


### Virtual environment

#### Установка
python -m venv myvenv

#### Запуск
C:\ts venv\scripts\sctivate

(venv) C:\ts>


- Установка зависимостей


- Требования к базе данных
## Установка PostgresSQL и pgadmin
- [How to install PostreSQL](https://www.enterprisedb.com/node/16#windows)

login-eldar
password-tkmlfhvehfnjd

_______________________________________________________________________________________________________________


# Creating the database

(venv) C:\ts> psql
#### Our > now changed into #, which means that we're now sending commands to PostgreSQL. Let's create a user with CREATE USER name;


### (remember to use the semicolon)

:# CREATE USER name;

:# CREATE DATABASE ts OWNER name;

### After this you need to download psycopg2.exe

pip install psycopg2

### After installing we need to applay migrations 

python manage.py migrate "module"

### And at the end we need to create superuser

python manage.py createsuperuser --username name


## Or you can use SQL shell and repeat al steps with them


_______________________________________________________________________________________________________________


# How to work with Django

# Migrations

python manage.py makemigrations "module"

python manage.py migrate "module"



# Freeze requirements.txt

(venv) C:\ts> pip install dj-database-url gunicorn whitenoise

(venv) C:\ts> pip freeze > requirements.txt

## Open this file and add the following line at the bottom:

psycopg2==2.7.2


# Procfile 

web: gunicorn mysite.wsgi --log-file -

# Create runtime.txt

python-3.6.4

# Change mysite/wsgi.py
Open the mysite/wsgi.py file and add these lines at the end:

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)


# Deploy on HEROKU

(venv) C:\ts>heroku create djangogirlsblog

(venv) C:\ts>git push heroku master

(venv) C:\ts>heroku ps:scale web=1

(venv) C:\ts>heroku open

(venv) C:\ts>heroku run python manage.py migrate

(venv) C:\ts>heroku run python manage.py createsuperuser


## Как контрибутить в проект

### Pushing

git status 

git add -A .  

git status  

git commit -m 'comment'

git push -u origin 'branch'    
_______________________________________________________________________________________________________________
### How to add new branch

git branch <branch name>

git checkout <branch name> 


### How to make pull rquest

после пуша заходим в Github на свою ветку и нажимаем pull request
_______________________________________________________________________________________________________________

## Структура проекта

### Описать каждый файл

Как называется проект, что в нём хранится

Как называется приложение, что в нём хранится

model.py

Типовой источник информации о ваших данных. Он содержит основные поля и поведение данных, которые вы храните. Как правило, каждая модель отображается в одну таблицу базы данных.

url.py
Четкая и элегантная схема URL-адресов - важная деталь высококачественного веб-приложения. Django позволяет создавать URL-адреса по своему усмотрению, без ограничений фреймворка.И в этом файле как раз таки и хранаться эти адреса

view.py

Вьюхи - это вызываемый объект, который принимает запрос и возвращает ответ. Это может быть больше, чем просто функция, и Django предоставляет пример некоторых классов, которые можно использовать как представления. Это позволяет вам структурировать представления и повторно использовать код, используя наследование.

# Pip

Django
django-extensions
psycopg2
dj-database-url
gunicorn 
whitenoise



_______________________________________________________________________________________________________________

