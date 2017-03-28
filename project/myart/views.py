from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render, redirect, render_to_response, HttpResponse
from .forms import UserLoginForm, UserRegisterForm, UploadForm, UploadImageForm
from django.template.context_processors import csrf
from myart.models import Msg, Painting, User
from django.contrib.auth.decorators import login_required
import os
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_list_or_404, get_object_or_404
from django.template import RequestContext

def home(request):
    return render(request, 'myart/home.html', {})
    
    
def Message(request):
    context = {}

    if 'submit' in request.POST:
        msg = Msg(name=request.POST['name'], email=request.POST['email'],
                     subject=request.POST['subject'], message=request.POST['message'])
        msg.save()
        context.update({'message': 'Message Received!', 'messagetype': 'success'})

    context.update(csrf(request))
    return render(request, 'myart/contact.html', context)
 
        
def login_view(request):
    print(request.user.is_authenticated())
    title = "Login" 
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
    	username = form.cleaned_data.get("username")
    	password = form.cleaned_data.get("password")
    	user = authenticate(username=username, password=password)
    	login(request, user)
    	return redirect("/")
    return render(request,"myart/form.html",{"form":form, "title": title})
	
def register_view(request):
    title = "Register"
    register = UserRegisterForm(request.POST or None)
    if register.is_valid():
        user = register.save(commit=False)
        password = register.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        print("registered Successfully")
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/")
        
    context = {
        "register": register,
        "title" : title
    }
    return render(request,"myart/register.html",context)
   

	
def logout_view(request):
    logout(request)
    return redirect("/")


def painting_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(request, 'myart/profile.html', {
        'form': form
    })


def pic_upload(request):
    if request.method == 'POST':
            form = UploadImageForm(request.POST, request.FILES)
            f_user= User.objects.get(id=request.user.id)
            f_profile_pic = form.cleaned_data.get['pic']
            p = User(user=f_user, pic=f_profile_pic)
            p.save()
            return redirect('home')
    else:
        form = UploadImageForm()
    return render(request, 'myart/profile.html', {
        'form': form
    })

def Show_painting(request, user_id):
    g = get_object_or_404(User, pk=user_id)
    i = Painting.objects.filter(user=g)
    return render_to_response('myart/preview.html', {'user': g, 'imagedata' :i }, context_instance=RequestContext(request))

def search_artist(request):
    return render(request, 'myart/home.html')
    
def search(request):
    error= False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            artist = User.objects.filter(name__icontains=q)
            return render(request, 'myart/search_results.html',
                      {'artist': artist, 'query': q})
    return render(request, 'myart/home.html', {'error': True})
    
def my_name(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username 
        name={"name": username}
    return render(request,'myart/profile.html',name)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'myart/pass.html', {
        'form': form
    })
    
def del_user(request):
    User.objects.get(id=request.user.id).delete()
    return render(request, 'myart/home.html', {})
