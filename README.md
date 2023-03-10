# PayS

## Тестовое задание

### Задача

Реализовать простой сервер с одной html страничкой, который общается со Stripe
(stripe.com/docs - платёжная система) и создает платёжные формы для товаров.
Для решения нужно использовать Django.

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:

- Django Модель Item с полями (name, description, price)
- API с двумя методами:
	- GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item;
	- GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить редирект на Checkout форму stripe.


## Вариант решения

Реализация выполнена на <a href='https://stripe.com/docs/payments/accept-a-payment?integration=checkout'>примере</a>.


## Запуск в Docker compose

Клонировать репозиторий. Подготовить файл .env (пример заполнения в env.template).
Собрать и запустить контейнер docker:


	$ docker-compose up --build

- Django Admin панель будет доступна по ссылке: http://0.0.0.0:8000/admin
- В админ панели можно создать объект Item

- Логин: admin
- Пароль: admin123


## Requirements

- django==4.1.7
- djangorestframework==3.14.0
- psycopg2-binary==2.9.5
- stripe==5.2.0

## Пример .env

	DJANGO_SECRET_KEY='django-...'

	POSTGRES_USER=postgres
	POSTGRES_PASSWORD=postgres
	POSTGRES_SERVER=db
	POSTGRES_PORT=5432
	POSTGRES_DB=postgres
	PGUSER=postgres

	STRIPE_PUBLISHABLE_KEY=pk_test_...
	STRIPE_SECRET_KEY=sk_test_...

	DJANGO_SUPERUSER_PASSWORD=admin123
	DJANGO_SUPERUSER_EMAIL=example@example.com
	DJANGO_SUPERUSER_USERNAME=admin
