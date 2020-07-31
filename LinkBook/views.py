from django.shortcuts import render,redirect,HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import Register
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import Book,Link
from newsapi import NewsApiClient
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    if request.method=='POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                username = form.cleaned_data["username"]
                book = Book(name='Random', author=request.user)
                book.save()
                messages.success(request, f'Account created for {username} ! ')
                return redirect('user')

    else:
        form = Register()
    return render(request, 'LinkBook/index.html', {'form':form})

def log_in(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('user')
        else:
            return redirect('LinkHome')
@login_required(login_url='LinkHome')
def create_book(request):
    if request.method=='POST':
        name = request.POST["name"]
        book = Book(name=name, author=request.user)
        book.save()
        messages.success(request, 'Your Book is created ')
        return redirect('userbooks')

@login_required(login_url='LinkHome')
def user_books(request):
    books = Book.objects.filter(author=request.user)
    leng = len(books)
    return render(request, 'LinkBook/books.html',{'books':books, 'leng':leng})

@login_required(login_url='LinkHome')
def user_links(request, id):
    book = Book.objects.filter(id=id).first()
    links = Link.objects.filter(book=book)
    le = len(links)
    return render(request, 'LinkBook/links.html', {'links':links, 'book':book,'le':le})

@login_required(login_url='LinkHome')
def delete_link(request, id):
    link = Link.objects.filter(id=id).first()
    id = link.book.pk
    link.delete()
    return redirect('userlinks',id)

@login_required(login_url='LinkHome')
def create_link(request):
    if request.method=='POST':
        books = Book.objects.filter(author=request.user)
        if len(books)==0:
            messages.warning(request,'create a book first')
            return redirect('user')
        book = Book.objects.filter(name=request.POST["select"]).first()
        link = Link(name=request.POST["namelink"], link=request.POST["url"], description=request.POST["desc"], book = book)
        link.save()
        id = book.pk
        messages.success(request, 'Link created')
        return redirect('userlinks', id)

@login_required(login_url='LinkHome')
def delete_book(request, id):
    book = Book.objects.filter(id=id).first()
    book.delete()
    return redirect('userbooks')

@login_required(login_url='LinkHome')
def user(request):
    books = Book.objects.filter(author=request.user)
    return render(request, 'LinkBook/user.html', {'books':books})

@login_required(login_url='LinkHome')
def trending(request):
    api_key = '3c8167b3dd0247889a79de38482f0f4b'
    newsapi = NewsApiClient(api_key=api_key)
    tophead = newsapi.get_top_headlines(country='in')
    l=tophead["articles"]
    desc , news, img, li= [],[],[],[]
    for i in range(len(l)):
        f=l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        li.append(f['url'])
    mylist = zip(news, desc, img, li)
    return render(request, 'LinkBook/trending.html', {'mylist':mylist})

def log_out(request):
    logout(request)
    return redirect('LinkHome')