from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Article

from django.shortcuts import render, redirect
from django.http import Http404
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if request.user.is_anonymous:
        raise Http404

    if request.method == "POST":
        form = {
            'text': request.POST["text"],
            'title': request.POST["title"]
        }

        if Article.objects.filter(title=form["title"]).exists():
            form['errors'] = "Статья с таким названием уже существует"
            return render(request, 'create_post.html', {'form': form})

        if form["text"] and form["title"]:
            article = Article.objects.create(
                text=form["text"],
                title=form["title"],
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
    else:
        return render(request, 'create_post.html', {})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if not (username and email and password):
            return render(request, 'register.html', {'error': 'Заполните все поля'})

        try:
            User.objects.get(username=username)
            return render(request, 'register.html', {'error': 'Пользователь уже существует'})
        except User.DoesNotExist:
            User.objects.create_user(username, email, password)
            return redirect('login')
    return render(request, 'register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('archive')
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'login.html')