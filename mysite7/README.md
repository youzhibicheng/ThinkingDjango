# How to create this sample

# PART 1 #

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

# PART 2 #

## 创建数据库 ##
解压 mysql 到 C:\mysql-5.6.29-winx64   
环境变量  
MYSQL\_HOME=C:\mysql-5.6.29-winx64  
Path中增加  
%MYSQL\_HOME%\bin  
修改配置文件my-default.ini,或者自己建立一个my.ini文件
[mysqld]  
basedir=C:\mysql-5.6.29-winx64  
datadir=C:\mysql-5.6.29-winx64\data  

以管理员身份运行cmd（一定要用管理员身份运行，不然权限不够）  
进入mysql的bin文件夹  
输入  
mysqld -install  
查看服务是否启动成功  
net start mysql  

先删除mysql（输入 mysqld -remove）再重新安装（输入 mysqld -install）  

mysqladmin -u root password 'passw0rd'  
mysql -u root --password=passw0rd  
create database mysite2  
use mysite2  

## 5. 后台配置MySQL数据库 ##
mysite/settings.py  
设置time zone  
创建数据库  
**python manage.py migrate**  
同时还需要安装  
**pip install MySQL-python**  
报错   
error: Microsoft Visual C++ 9.0 is required (Unable to find vcvarsall.bat). Get it from http://aka.ms/vcpython27  
解决方法  
根据提示去 http://aka.ms/vcpython27 下载  
**VCForPython27.msi**  
win7 64 安装mysql-python：_mysql.c(42) : fatal error C1083: Cannot open include file: 'config-win.h': No such file or directory  
需要下载  
**MySQL-python-1.2.5.win32-py2.7.exe**  
https://pypi.python.org/pypi/MySQL-python  


## 6. Creating Model ##
polls/models.py

## 7. Activating models ##
mysite/settings.py  
INSTALLED_APPS = [  
'polls.apps.PollsConfig',  
'django.contrib.admin',  
'django.contrib.auth',   
'django.contrib.contenttypes',  
'django.contrib.sessions',  
'django.contrib.messages',  
'django.contrib.staticfiles',  
]  
**python manage.py makemigrations polls**  
生成文件  polls/migrations/0001_initial.py  
运行命令  
**python manage.py sqlmigrate polls 0001**  
会生成相应的SQL脚本  
**python manage.py check**  
**python manage.py migrate**
在数据库库中创建表

remember the three-step guide to making model changes:  
• Change your models (in models.py).  
• Run python manage.py makemigrations to create migrations for those changes  
• Run python manage.py migrate to apply those changes to the database.  



## 8. Playing with the API ##
python manage.py shell  
from polls.models import Question, Choice  
Question.objects.all()  
from django.utils import timezone  
q = Question(question_text="What's new?", pub_date=timezone.now())  
q.save()  
重写 \__str__() 需要退出，然后重新 python manage.py shell才生效  

## 9. 使用django admin ##
python manage.py createsuperuser  
james / youzhibicheng@163.com / passw0rd  
python manage.py runserver  
http://127.0.0.1:8000/admin  
让数据库表可编辑  
polls/admin.py


# PART 3 #
polls/views.py  
polls/urls.py  
polls/templates/polls/index.html  
polls/templates/polls/detail.html
mysite/settings.py  
----修改 TEMPLATES



# PART 4 #
focus on simple form processing  
polls/templates/polls/detail.html  
polla/views.py

## 4.2 Use generic views: Less code is better ##
polls/url.py  
polls/views.py  

# PART 5 #
create automatic tests  
polls/tests.py  
**$ python manage.py test polls**  

test a view



# PART 6 #
add a stylesheet and an image  
**Customize your app’s look and feel**  
mysite/settings.py  
----STATICFILES_FINDERS  
polls/static/polls/style.css
polls/static/polls/images/
polls/templates/polls/index.html  

# PART 7 #
**customizing the Django’s automatically-generated admin site**  
## Customize the admin form ##
polls/admin.py  
Customize the admin change list  
Customize the admin look and feel  
 Customize the admin index page  

# PART 8 : Advanced tutorial: How to write reusable apps #

