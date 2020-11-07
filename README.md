
# Проект TopSkills

## Требования для начала работы

- Python 3, pip, git, Visual Studio Code
- Аккаунт Github
- Скинуть Эльдару почту от аккаунта GitHub для добавление в контрибуторов проекта

## Как контрибутить в проект

### Как пушить код

Проверка изменённых файлов. Делать перед каждым пушем!
```
git status 
```

Если все файлы можно добавить, то добавить их этой команндой. Или добавлять файлы по отдельности.
```
git add -A .
```

Снова проверить, что все нужные файлы добавлены в коммит.
```
git status
```

После, написать комментарий коммита. Стандарт сообщения коммита такой: начинать с глагола, и писать, чтобы было добавлено или изменено.
Если это промежуточный коммит, то разрешается оставлять комментарий "wit". Что значит work-in-progress.
```
git commit -m 'Added new comment'

git push -u origin branch_name
```

### Мердж в мастер. Создание pull request
1. Делаются все коммиты в ветку
2. Создается pull request через github.com. После пуша заходим в Github на свою ветку и нажимаем "pull request"
3. Желательно, чтобы кто-нибудь другой посмотрел код pull request'a
4. Убирается конфлиты, если они есть
5. Ветка мерджится с мастером
6. Ветка удаляется


### Как создавать ветки
Пушить в мастер разрешается в очень редких случаях.
Ветка называется по названии фичи, надо которой будут работать в ней.

```
git checkout -b branch name
```

### Переключение на ветку
```
git checkout branch_name
```
## Начало работы с проектом

### Клонирования проекта
```
git clone https://github.com/MuratovER/ts.git
```

### Проверка наличия Python
```
python3 --version
```

## Virtual environment (venv)
Обязательное условие для работы с Python проектами это виртуальная среда для избежания конфликта зависимостей.

#### Cоздание venv
Linux
```
python3 -m venv venv
```

Windows
```
C:\topskills> python -m venv venv
```

#### Запуск
Windows
```
C:\topskills venv\scripts\activate
```

Linux
```
source venv/bin/activate
```

Название venv в начале командной строки говорит о том, что вирутальная среда активирована
(venv) C:\ts>


### Установка зависимостей проекта
```
pip install -r requirements.txt
```

## База данных

### Требования к базе данных
Возможно использование SQLite. Это не требует установки, однако если ты занимаешься backend разработкой, то рекомендуется установить PostgreSQL.

Для использования SQLite поменяй database backend ```settings.py```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

### Установка PostgresSQL и pgadmin
- [How to install PostreSQL](https://www.postgresqltutorial.com/install-postgresql/)

Для работы с базой данных можно использовать встроенную консоль ```psql``` или установить [pgAdmin 4](https://www.pgadmin.org/download/pgadmin-4-windows/)

Пользователь, которого нужно создать:

login: ```eldar```

password: ```tkmlfhvehfnjd```

### Создание базы данных

Открыть консоль

Windows
```
(venv) C:\ts> psql
```

Linux
```
psql
```


Ввести команды для создания пользователя и содания базы данных
```
CREATE USER eldar;

ALTER USER eldar WITH PASSWORD 'tkmlfhvehfnjd';

CREATE DATABASE ts OWNER eldar;
```


### Команды для создания таблиц в базе данных
После установки и создания базы данных, нужно указать команду Django для создания таблиц

```
python manage.py migrate
```


## Работа с Django

### Migrations
```

python manage.py makemigrations

python manage.py migrate
```

### Создание суперпользователя Django
```
python manage.py createsuperuser
```

# Сохранение зависимостей в requirements.txt
```
(venv) C:\ts> pip freeze > requirements.txt
```
## Установка зависимостей с добавлением названия зависимости и её версии

(venv) C:\ts> pip install dj-database-url gunicorn whitenoise

psycopg2==2.7.2

## Deploy on HEROKU

```
(venv) C:\ts>heroku create djangogirlsblog

(venv) C:\ts>git push heroku master

(venv) C:\ts>heroku ps:scale web=1

(venv) C:\ts>heroku open

(venv) C:\ts>heroku run python manage.py migrate

(venv) C:\ts>heroku run python manage.py createsuperuser
```

## Команды Django
```
# сбор статик файлов
python manage.py collectstatic


```


## Структура проекта


**model.py**

> Типовой источник информации о ваших данных. Он содержит основные поля и поведение данных, которые вы храните. Как правило, каждая модель отображается в одну таблицу базы данных.

**url.py**
>Четкая и элегантная схема URL-адресов - важная деталь высококачественного веб-приложения. Django позволяет создавать URL-адреса по своему усмотрению, без ограничений фреймворка.И в этом файле как раз таки и хранаться эти адреса

**view.py**

> Вьюхи - это вызываемый объект, который принимает запрос и возвращает ответ. Это может быть больше, чем просто функция, и Django предоставляет пример некоторых классов, которые можно использовать как представления. Это позволяет вам структурировать представления и повторно использовать код, используя наследование.

## Шаблоны
Шаблоны работают по принципу 2-ух шаблонов
Основной base.html и к нему прикручиваются другие шаблоны


Шаблоны распологаются в ```mainsite/templates```
Для того чтобы шаблон успешно отправил данные в base.html необходимо прописать данные строки 

```
{% extends 'mainsite/base.html' %} 
{% block content %}
здесь пишеться ваша разметка
{% endblock %}
```

## Статические файлы
Статические файлы храняться в папке ```ts/mainsite/static```