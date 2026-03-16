from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import RegisterForm, LoginForm, PostForm, CommentForm


def home(request):
    query = request.GET.get('q')
    posts = Post.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(title__icontains=query)

    return render(request, 'home.html', {
        'posts': posts,
        'query': query
    })


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    error = ''

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error = 'Hibás felhasználónév vagy jelszó.'
    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form,
        'error': error
    })


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'new_post.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', post_id=post.id)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('home')


@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'my_posts.html', {'posts': posts})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        return redirect('my_posts')

    return render(request, 'delete_post.html', {'post': post})
