# python-Django-crud


pip install virtualenv
pip install django
virtualenv env
.\env\Scripts\activate
.\env\Scripts\deactivatde.bat
pip list
django-admin startproject techno
python manage.py startapp technoAdminApp





python manage.py migrate 
localhost:3000/admin
python manage.py createsuperuser



# models.py

class PostTable(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)


python manage.py makemigrations
python manage.py migrate 


# admin.py
# Register your models here.
from . models import PostTable
admin.site.register(PostTable)


localhost:3000/admin

username: gimhana
password: gimhana
