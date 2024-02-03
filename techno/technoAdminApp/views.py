from django.shortcuts import render, redirect
from . models import PostTable
from . form import createPost

# Create your views here.
def posts(req):
    database = PostTable.objects.all()
    return render(req, 'main.html', {'database': database})
def post(req, pid):
    db = PostTable.objects.get(id=pid)
    return render(req, 'post.html', {'db': db})

def createNewPost(req):
    form= createPost()
    if req.method == 'POST':
        form = createPost(req.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    return render(req, 'form.html', {'form': form})

def updatePost(req, pid):
    db = PostTable.objects.get(id=pid)
    form=createPost(instance=db)
    if req.method == 'POST':
        form= createPost(req.POST, instance=db)
        if form.is_valid():
            form.save()
            return redirect('posts')
    return render(req, 'form.html',  {'form': form})

def delete(request, pid):
    database= PostTable.objects.get(id=pid)
    if request.method == 'POST':
        database.delete()
        return redirect('posts')
    return render(request, 'del.html')