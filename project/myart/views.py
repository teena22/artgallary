from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm

def home(request):
    return render(request, 'myart/home.html', {})
    
def contact(request):
    return render(request, 'myart/contact.html', {})
        
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

