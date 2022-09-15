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

Чтобы зайти в админ-панель
```python
http://127.0.0.1:8000/admin
```
Для регистрации пользователей
```python
http://127.0.0.1:8000/api/user/register/
```

Авториация
```python
http://127.0.0.1:8000/api/user/login/
```
Список всех пользователей
```python
http://127.0.0.1:8000/api/user/list/
```
Чтобы удалить пользователя в конце укажите id пользователя

```python
http://127.0.0.1:8000/api/user/delete/1/
```
Чтобы вывести все детали о пользователя убедитесь что вы авторизованы
```python
http://127.0.0.1:8000/api/user/detail/1/
```

Создать пост о продукте
```python
http://127.0.0.1:8000/api/product/create/
```