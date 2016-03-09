# How to create this sample
## 1. create project ##
django-admin startproject mysite  
cd mysite
## 2. start server ##
python manage.py runserver  
http://127.0.0.1:8000  
如果更改端口  
python manage.py runserver 8080
## 3. create app ##
python manage.py startapp polls
## 4. create view ##
polls/views.py  
polls/urls.py  
mysite/urls.py
