from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import movie

from . forms import movieform
def index(request):
    cabs = movie.objects.all()
    context1 = {
        'movie_value': cabs
    }
    return render(request, 'basic.html', context1)


def detail(request, movie_id):
    mov = movie.objects.get(id=movie_id)
    return render(request, "details.html", {'movie': mov})

def addmovie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        year=request.POST.get('year')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        mve=movie(name=name,year=year,desc=desc,img=img)
        mve.save()
    return render(request,'add.html')

def update(request,id):
    mve=movie.objects.get(id=id)
    frm=movieform(request.POST or None,request.FILES,instance=mve)
    if frm.is_valid():
        frm.save()
        return redirect('/')
    return render(request,'edit.html',{'frm':frm,'mve':mve})
def delete(request,id):
    if request.method=='POST':
        mvee=movie.objects.get(id=id)
        mvee.delete()
        return redirect('/')
    return render(request,'delete.html')