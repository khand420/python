
       *1. STEP TO CREATE VIRTUAL ENVIRONMENT
pip install virtualenv
1  python -m venv env/myenv
2  .\env\myenv\Scripts\Activate

3 pip install "Django==3.0.*"
4.pip freeze > requirements.txt
 pip install -r requirements.txt

5 django-admin startproject Registration
6 django-admin startapp account

7 python manage.py createsuperuser
8.python manage.py makemigrations
9.python manage.py migrate


        *2. FOR UPGRADING PIP
python -m pip install --upgrade pip



        *3. additional lacalhost(code2hell.in) in host.txt in like given below. your path-> C:\Windows\System32\drivers\etc
# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost

    127.0.0.1       code2hell.in


         *4. for TLS(Transport Layer Services)- it is use to https//:
install using pip 
django-extensions==2.2.5  (third paty custom extension in django)
django-extensions==2.2.5
werkzeug==0.16.0
pyOpenSSL==19.0.0

for checking ssl certificate check using command:
python manage.py runserver_plus --cert-file cert.crt


*5 RUNNING ON SERVER PORT
http://code2hell.in:8000/account/login/?next=/account/







*********BLOG********


*7 SEND EMAIL USING SMTP SERVER using command

1.python manage.py shell
2.from django.core.mail import send_mail                               sender                reciever      
3.send_mail('Django mail', 'This e-mail was sent with Django','khand7661@gmail.com',['khand7661gmail.com'], fail_silently=false)
4. go to search on google-> myaccount.google.com /security /less secure app access(turn on)
5. now enter step3, output=1-> it show success message


*8 RECOMMENDING A SIMMILAR POST (for tags)
pip install django_taggit
add tag using shell 
1.from blog.models import Post
2.post = Post.objects.get(id=2)
3.print(post)
4.post.tags.add('music','jazz','django)
5.post.tags.all()
6.post.tags.remove('django')


*For editing content part in the database use markdown
pip install markdown


*AFTER INSTALLING postgrsql DB of django setting be like..

'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'khand',
        'USER': 'blog',
        'PASSWORD':'khand'
pip install psycopgy2-binary ==2.8.4 -> help to seach query      



*** HOST ON HEROKU  using cli waitress ****
1. heroku login
2. git init 
3. git add . 
4. git commit -m "Initial Commit"
5. heroku create code2hell
6. heroku git:remote -a code2hell
7. pip install waitress
8. for check RUN-> waitress-serve --port=8000 code2hell.wsgi:application
9. CREAT Procfile and write (web: waitress-serve ---port=8000 code2hell.wsgi:application)
10. pip install whitenoise==5.2.0 and ADD in setting middlware ('whitenoise.middleware.WhiteNoiseMiddleware',) just below middleware.security
11. ADD setting host like  ["code2hell.herokuapp.com","localhost"]
12. NOW Procfile be like(web: waitress-serve ---port=$PORT code2hell.wsgi:application)

13. git add . 
14. git commit -m "second commit"
15. git push heroku
heroku config:set DISABLE_COLLECTSTATIC=1
git push heroku main

edit Procfile
git add -A 
git commit -m "procfile"
git push heroku main


heroku login
heroku git:remote -a code2hell
git add -A 
git commit -m "Initial commit"
git push heroku main


python manage.py dumpdata --exclude auth.permission --exclude blog --exclude home > data.json
heroku run python manage.py loaddata data.json
or
# 1: Dump your json
$ python manage.py dumpdata --all > ./mydump.json

# 2: dump your schema
$ python manage.py sqlflush > schema.sql


python manage.py dumpdata > db.json
Change the database settings to new database such as of MySQL / PostgreSQL.
python manage.py migrate
python manage.py shell 
Enter the following in the shell
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
python manage.py loaddata db.json

python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > data.json


**************GITHUB*****************
or create a new repository on the command line
echo "# ShopingCart-API" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/khand420/ShopingCart-API.git
git push -u origin main


…or push an existing repository from the command line
git remote add origin https://github.com/khand420/ShopingCart-API.git
git branch -M main
git push -u origin main
