from django.forms import ModelForm
from . models import PostTable

class createPost(ModelForm):
    class Meta():
        model=PostTable
        fields= '__all__'