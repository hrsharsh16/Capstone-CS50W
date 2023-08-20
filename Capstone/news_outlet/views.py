from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse

from .forms import CustomUserCreationForm
from .models import User

# Create your views here.
def index(request):
    return render(request, 'news_outlet/index.html')

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


def reader_dashboard(request):
    return render(request, 'news_outlet/reader_dashboard.html')

def admin_dashboard(request):
    return render(request, 'news_outlet/admin_dashboard.html')
        

