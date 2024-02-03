from django.shortcuts import render
from . models import PostTable


# Create your views here.
def posts(req):
    database = PostTable.objects.all()
    return render(req, 'main.html', {'database': database})
def post(req, pid):
    return render(req, 'post.html')