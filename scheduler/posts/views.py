from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib.auth.views import LoginView, LogoutView

@login_required
def schedule_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Do not save yet
            post.user = request.user  # Assign the logged-in user
            post.save()  # Now save
            return redirect('dashboard')  # Redirect after saving
    else:
        form = PostForm()
    
    return render(request, 'posts/schedule_post.html', {'form': form})

@login_required
def dashboard(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'posts/dashboard.html', {'posts': posts})

def home(request):
    return render(request, 'posts/home.html')

class CustomLoginView(LoginView):
    template_name = 'posts/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'

# Remove @login_required
def dashboard(request):
    posts = Post.objects.all()  # Show all posts publicly
    return render(request, 'posts/dashboard.html', {'posts': posts})
