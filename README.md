TodoWoo - Django Project with REST API and Token Authentication
======

TodoWoo is a web application that create a ToDo List. The application has a Rest API built with Django Rest Framework - DRF.
The API allow us to manipulate all application via CUrl commands, without the need to access the graphical interface generated by the DRF.
------
The API and the JSon Web Token - JWT Login, was developed by me during the course "Creating Python APIs Like a BOSS" by ZappyCode.
The  web application already has been created by Nick from ZappyCode. So our task was to create an API for an existing application.

Course:
[Creating Python APIs Like a BOSS - The Django REST Framework](https://zappycode.com/courses/creating-apis-with-the-django-rest-framework-python)

## Screenshots

- Home Page
![](Screenshots/Home.png)
&nbsp;
- Creating a New Todo
![](Screenshots/new_todo.png)
&nbsp;
- Creating a new user through CUrl Comand and Receive the User's Token
```
curl -X "POST" http://127.0.0.1:8000/api/signup -H 'Content-Type: application/json' -d '{"username":"test_user","password":"abc123"}'
```
![](Screenshots/new-user.png)
&nbsp;
- Creating a new ToDo through CUrl
```
curl -X "POST" http://127.0.0.1:8000/api/todos -H 'Content-Type: application/json' -H 'Authorization: Token 4c38b8e43682f5d2e4046ff2545fb349a6e4ca87' -d '{"title": "ToDoTest","memo": "","important": true}'
```
![](Screenshots/new_todo2.png)
  
## Getting started

To run the project, you will need to install the following software:

- [Python 3.9.*: Required to run the Python project](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe)
- [Django 3.1.*:  A Python Web framework.](https://pypi.org/project/Django/)
- [Django REST framework: A powerful and flexible toolkit for building Web API.](https://www.django-rest-framework.org/)

### Features

- [x] Create ToDo
- [X] Complete ToDo  
- [x] Delete ToDo

## Authors

Marcos Garcia   
e-mail: mvrgarcia05@gmail.com
