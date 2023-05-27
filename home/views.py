from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django import forms

from django.contrib.auth.models import User
from django.contrib import auth
#username=admin,password=12345
#for login use this{username:abc,password:123456},{username:asd,password:456}
#see in users
# Create your views here.
def index(request):
    
    
    return render(request,'index.html')
    #return HttpResponse("yeahhh!")
def services(request):
    return render(request,'services.html')
def contact(request):
    print(request.method)
    if request.method=="POST":
        email=request.POST.get('email')
        
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(email=email,name=name,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent')
    return render(request,'contact.html')
def loginUser(request):
    """class InputForm(forms.Form):
   
        username = forms.CharField(max_length = 200, widget= forms.TextInput
                           (attrs={'placeholder':'Enter your username'}))
        password= forms.CharField(max_length = 8, widget= forms.PasswordInput
                           (attrs={'placeholder':'Enter your password'}))
    context ={}
    context['form']= InputForm()"""
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('special')
        else:
            messages.success(request, 'Username or password is incorrect!')
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')
def register(request):
    """class InputForm(forms.Form):
        email=forms.CharField(max_length=100,
                           widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))
        username = forms.CharField(max_length = 200, widget= forms.TextInput
                           (attrs={'placeholder':'Enter your username'}))
        password1= forms.CharField(max_length = 8, widget= forms.PasswordInput
                           (attrs={'placeholder':'Enter your password'}))
        password2 = forms.CharField(max_length = 8, widget= forms.PasswordInput
                           (attrs={'placeholder':'Renter your password'}))
        
    context ={}
    context['form']= InputForm()"""
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'register.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('special.html')
        else:
            messages.success(request, 'Password does not match!')
            return render (request,'register.html', {'error':'Password does not match!'})
    else:
        return render(request,'register.html')
def special(request):
    return render(request,'special.html')
def logoutUser(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('/')
def cart(request):
    return render(request,"cart.html")
def wishlist(request):
    return render(request,"wishlist.html")

