from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm
from django.contrib import messages
import requests
from .api_key import MY_API_KEY
# from django.contrib import messages
from .models import User, ProfilePhoto, Book, BookImage
from django.contrib.auth.models import User as Uzer
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from pexels_api import API
import random

def base(request):
    return render(request, 'base.html')

def home(request):
    logouter = request.POST.get('logout', '')
    print(request.user.username)
    if logouter == '':
        return render(request, 'before_login/home.html', {'name': request.user.username})
    else:
        logout(request)
        messages.success(request, "User logged out")
        return render(request, 'before_login/home.html', {'name': request.user.username})

def hello(request):
    return HttpResponse('hello there')

def library(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    else:
        currentuser = User.objects.filter(username=request.user.username).first()
        books = Book.objects.all().prefetch_related('book_image','author','publisher')
        if len(books)>0:
            print(books)
        return render(
            request, 
            'after_login/library.html',           
            {'name': request.user.username, 'currentuser': currentuser, 'books': books}
        )

def user_login(request):
    if not request.user.is_authenticated:
        print(request.POST)
        searcher = request.POST.get('username', '')
        if(searcher == ''):
            return render(request, 'before_login/login.html')
        else:
            username=request.POST.get('username', '')
            password=request.POST.get('password', '')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successful Login")
                return HttpResponseRedirect('/library')
            else:
                messages.warning(request, "Invalid Login Credentials")
                return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/library')

def user_register(request):
    form = RegisterForm()
    print(request.POST)
    print(request.FILES)
    searcher = request.POST.get('name', '')
    if request.user.is_authenticated:
        return HttpResponseRedirect('/library')
    if(searcher == ''):
        return render(request, 'before_login/register.html', {'form': form })
    else:
        if(form.is_valid and form.is_multipart):
            if Uzer.objects.filter(username = request.POST.get('username', '')).first() or User.objects.filter(username = request.POST.get('username', '')).first():
                messages.error(request, "This username is already taken")
                return HttpResponseRedirect('/user_register')
            else:
                myuser = Uzer.objects.create_user(
                    username=request.POST.get('username', ''),
                    email=request.POST.get('email', ''),
                    password=request.POST.get('password', '')
                )
                myuser.save()
                myphoto = ProfilePhoto.objects.create(
                    image=request.FILES.get('profile_pic', '')
                )
                dbdetails = User.objects.create(
                    name=request.POST.get('name', ''),
                    username=request.POST.get('username', ''),
                    email=request.POST.get('email', ''),
                    gender=request.POST.get('gender', ''),
                    profile_pic=myphoto 
                )
                dbdetails.save()
                myphoto.save()
                messages.success(request, "User created.")
                return HttpResponseRedirect('/library')
        else:
            return HttpResponseRedirect('/user_register')

def simple_gallery(request):
    api = API(MY_API_KEY)
    api.curated(results_per_page=150)
    photos = api.get_entries()
    if(photos):
        random.shuffle(photos)
    return render(request, 'before_login/simple_gallery.html', {'photos': photos})

def random_activity(request):
    req = requests.get('https://www.boredapi.com/api/activity')
    random_activity = req.json()
    if(random_activity):
        print(random_activity)
        # return HttpResponseRedirect(reverse('account:profile'))
    return render(request, 'before_login/random_activity.html', {'random_activity': random_activity})

def search_gallery(request):
    searcher = request.POST.get('searcher', '')
    if searcher == '':
        return HttpResponseRedirect('/simple_gallery')
    else:
        api = API(MY_API_KEY)
        api.search(request.POST['searcher'], page=1, results_per_page=200)
        photos = api.get_entries()
        if(photos):
            print('here')
            random.shuffle(photos)
        return render(request, 'before_login/search_gallery.html', {'photos': photos, 'searcher': searcher})
    # req = requests.get('https://www.boredapi.com/api/activity')
    # random_activity = req.json()
    # if(random_activity):
    #     print(random_activity)
    # return render(request, 'before_login/random_activity.html')