from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import CustomUserCreationForm
from .models import User, Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {'articles': articles}
    return render(request, 'news_outlet/index.html', context)

class CustomLoginView(LoginView):
    template_name = 'news_outlet/login.html'  # Replace with your login template

    def get_success_url(self):
        if self.request.user.user_type == 'reader':
            return reverse('reader_dashboard')  # URL for the reader dashboard
        elif self.request.user.user_type == 'admin':
            return reverse('admin_dashboard')   # URL for the admin dashboard
        else:
            return reverse('index')  # Fallback URL
        
class CustomLogoutView(LogoutView):
    next_page = 'index'  # URL for the landing page after logout


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.user_type = 'reader'  # Set default user type
            user_instance.save()
            login(request, user_instance)
            return redirect('index')  # Redirect to the desired page after registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'news_outlet/register.html', {'form': form})

@login_required
def reader_dashboard(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {'articles': articles}
    return render(request, 'news_outlet/reader_dashboard.html', context)


@login_required
def admin_dashboard(request):
    articles = Article.objects.filter(author=request.user).order_by("-created_at")
    context = {'articles': articles}
    return render(request, 'news_outlet/admin_dashboard.html', context)


@login_required        
def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(author=request.user, title=title, content=content)
        return redirect('admin_dashboard')  # Redirect to the admin dashboard after article creation
    
    return render(request, 'news_outlet/admin_dashboard.html')



def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=article)

    if request.method == 'POST':
        if request.user.is_authenticated:
            content = request.POST['content']
            comment = Comment(article=article, author=request.user, content=content)
            comment.save()
            return redirect('article_detail', pk=pk)

    context = {'article': article, 'comments': comments}
    return render(request, 'news_outlet/article_detail.html', context)


def search(request):
    query = request.GET.get('q')  # Get the search query from the URL parameter
    articles = Article.objects.filter(title__icontains=query) if query else []
    context = {'query': query, 'articles': articles}
    return render(request, 'news_outlet/search_results.html', context)


@login_required
def save_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    user = request.user

    if request.method == 'POST':
        if article in user.bookmarked_articles.all():
            user.bookmarked_articles.remove(article)
            result = "deleted"
        else:
            user.bookmarked_articles.add(article)
            result = "saved"

        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request'})