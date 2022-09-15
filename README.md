# Создание REST API с помощью Python, Django
В примере используется веб-платформа Django и пакет инфраструктуры Django Rest для простой реализации REST API

### Загрузите пример кода
```python 
git clone https://github.com/Nurmurok/project_crm.git
```
### Зайдите в project_crm
```python
cd project_crm
```
### Установите venv
```python
python3 -m venv venv
```
```python
.\venv\Scripts\activate
```
Вы можете установить все необходимые пакеты за один раз, выполнив приведенную ниже команду :
```python
pip install -r requirements.txt
```
# Запустить образец локально
____
Выполните приведенную ниже команду, чтобы запустить веб-сервер разработки на локальном компьютере. По умолчанию сервер работает на порту 8000 с IP-адресом 127.0.0.1. Вы можете явно указать IP-адрес и номер порта.

Выполните приведенную ниже команду, чтобы запустить веб-сервер разработки на локальном компьютере. По умолчанию сервер работает на порту 8000 с IP-адресом 127.0.0.1. Вы можете явно указать IP-адрес и номер порта.
```python
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```
а потом запустить сервер
```python
python manage.py runserver
```

Когда приложение Django запустится, вы увидите что-то вроде:



```python
...
System check identified no issues (0 silenced).
September 15, 2022 - 15:55:25
Django version 4.1.1, using settings 'crm_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
## Проект состоит из трёх  приложений : accounting(бухгалтерский учёт), user(клиентская база) и product(продуктовая база)

#### Чтобы зайти в админ-панель:
```python
http://127.0.0.1:8000/admin
```
#### Для регистрации пользователей:
```python
http://127.0.0.1:8000/api/user/register/
```

#### Авториация:
```python
http://127.0.0.1:8000/api/user/login/
```
#### Список всех пользователей и поиск по username и email, так же есть пагинация:
```python
http://127.0.0.1:8000/api/user/list/
```
#### Чтобы удалить пользователя в конце укажите id пользователя:

```python
http://127.0.0.1:8000/api/user/delete/1/
```
#### Чтобы вывести все детали о пользователя убедитесь что вы авторизованы:
```python
http://127.0.0.1:8000/api/user/detail/1/
```

#### Создать категорию ,продукт:
```python
http://127.0.0.1:8000/api/product/cat_create/
http://127.0.0.1:8000/api/product/create/
```
#### Для вывода списка продуктов и фильтры по категориям и стоимости :
```python
http://127.0.0.1:8000/api/product/list/
```

#### Detail,Update,Delete:
```python
http://127.0.0.1:8000/api/product/detail/2/

http://127.0.0.1:8000/api/product/update/2/

http://127.0.0.1:8000/api/product/delete/2/
```
#### Список категорий:
```python
http://127.0.0.1:8000/api/product/category_list
```

#### Фильр по категориям и стоимости, подбирает продукты той категории что вы указали и по цене от указанного и выше
```python
http://127.0.0.1:8000/api/product/filterByCategory/Phones/40000/
```

#### Для вывода статистики 
```python
http://127.0.0.1:8000/api/accounting/statistics/
```
#### Вы увидете что-то вроде 
```python
{
    "user_count": 2,
    "product_count": 3,
    "min_price": 40000,
    "max_price": 80000,
    "avg_price": 56666.666666666664,
    "all_sum": 200000
}
```
### Полезные ссылки для подробного изучения изучения DJANGO REST
- https://www.django-rest-framework.org/
- https://www.django-rest-framework.org/api-guide/filtering/
- https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html
