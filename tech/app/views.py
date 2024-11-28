from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(req):
    return render(req,'home.html')




def About(req):
    return render(req,'about.html')


def courses(req):
    data=course.objects.all()
    return render (req,'course.html',{'courses':data})


def view_courses(req,c_id):
    data=course.objects.get(pk=c_id)
    return render(req,'view_course.html',{'courses':data})


def Contact(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        message=req.POST['message']
        data=contact.objects.create(name=name,email=email,message=message)
        data.save()
        return redirect(Contact)
    else:
        return render (req,'contact.html')
    