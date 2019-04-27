from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import post
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms


def post_detail(request,id):
    posta=post.objects.get(id=id)
    user = User.objects.exclude(id=request.user.id)
    return render(request,'post/detail.html',{'posta':posta,'user':user})
def post_index(request):
     users = User.objects.exclude(id=request.user.id)
     posts=post.objects.all()
     args = {
             'posts': posts, 'users': users, 
        }
   
     return render(request,'post/index.html',args)
def post_create(request):

    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post = form.save()
        post.user = request.user
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())
   
    context={
        'form':form,
        }
    return render(request,'post/form.html',context)

    
def post_delete(request):
    return HttpResponse('<b>post_delete</b>')  

def post_update(request):
    return HttpResponse('<b>post_update</b>')


