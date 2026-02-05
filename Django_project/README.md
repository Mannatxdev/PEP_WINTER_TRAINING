## Making new folder and server start
1. mkdir (folder name == Django_project)
2. django-admin startproject  myapp Django_project
3. python manage.py migrate
4. cd Django_project
5. python manage.py runserver 


## Creating supper User
1. python manage.py migrate
2. python manage.py createsuperuser
3. python manage.py runserver


## To run Templates(ALL HTML FILES)
1. Django_project => myapp => setting.py => TEMPLATES => DIRS => 'templates' in string name of folder.


## To run server 
1. .venv\scripts\activate
2. cd django_project
3. python manage.py runserver


## To run static files (css)
1. settings =>
2.    import os
3.    STATIC_URL = '/static'
4.    STATICFILES_DIRS = [ os.path.join(BASE_DIR,'static')]



## 04/01/26 goal ##
1. project creation
2. app creation
3. creating superuser adding it and showing on the page
4. taking input from user for name password etc

