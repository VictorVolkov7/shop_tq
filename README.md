# **Product market**

Это проект, написанный на языке:

- Python 3.12

С использованием библиотек/фреймворков:
- Django 5.0.7
- Django REST framework 3.15.2
- drf-spectacular 0.27.2
- PostgreSQL


Backend-составляющая магазина продуктов с Django admin интерфейсом и API для просмотра категорий, продуктов и управления
корзины, а также регистрации и аутентификацией пользователей. 


## **Установка**
### Для установки проекта Product market, следуйте инструкциям ниже:

**<p>1. Сделайте Fork этого репозитория. Репозиторий появится в ваших личных репозиториях на GitHub.</p>**

**1.1 Сделайте `git clone` форкнутого репозитория, чтобы получить репозиторий локально:**

**<p>2. Перейдите в папку с проектом.</p>**

**<p>3. Создайте и активируйте виртуальное окружение:</p>**

`poetry init`

`poetry shell`

**<p>4. Установите зависимости проекта:</p>**

`poetry install`

**<p>5. Создайте файл .env в корневой папке проекта (shop_testovoe/) и заполните данные для настройки проекта из файла .env.sample:</p>**

```ini
# Django settings
DJANGO_SECRET_KEY=django secret key

# PostgreSQL settings
POSTGRES_DB=db name
POSTGRES_USER=psql username
POSTGRES_PASSWORD=psql password
POSTGRES_HOST=host for db
POSTGRES_PORT=port for db

# Superuser creation
SU_EMAIL=your_email@gmail.com
SU_PASSWORD=your_password
```

**<p>6. Примените миграции:</p>**

`python manage.py migrate`

**<p>7. Воспользуйтесь командой для установки русского языка:</p>**

`django-admin compilemessages`

**<p>8. ЗАПУСК BACKEND-ЧАСТИ: Запустите сервер:</p>**

`python manage.py runserver` или настройте запуск Django сервера в настройках.


Таким образом можно работать с backend-частью локально для отладки.

После запуска сервера. Вы сможете перейти на сайт с документацией http://127.0.0.1:8000/api/docs/ 
(если сервер запущен локально), и начать пользоваться всеми API методами проекта. 

Также вы можете схему данных .yaml файлом по адресу http://127.0.0.1:8000/api/schema/ (если сервер запущен локально).

### Либо с помощью Docker
**<p>1. Измените файл .env в корневой папке проекта (shop_testovoe/), заменив значение в стрчке "POSTGRES_HOST" на Ваше название 
контейнера с базой данных":</p>**
```ini
/.env/

# Django settings
DJANGO_SECRET_KEY=django secret key

# PostgreSQL settings
POSTGRES_DB=db name
POSTGRES_USER=psql username
POSTGRES_PASSWORD=psql password
POSTGRES_HOST=container name
POSTGRES_PORT=port for db

# Superuser creation
SU_EMAIL=your_email@gmail.com
SU_PASSWORD=your_password
```

**<p>2. ЗАПУСК BACKEND-ЧАСТИ:: Воспользуйтесь командами:</p>**

`docker compose build` для создания оптимального билда проекта.

`docker compose up` для запуска docker compose контейнера.




## **Использование**
#### На проекте реализована регистрация новых пользователей через API.
Также есть команда для создания суперпользователя `python manage.py csu` с данными из .env файла


Автор
VictorVolkov7 - vektorn1212@gmail.com