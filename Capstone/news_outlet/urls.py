from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('reader_dashboard/', views.reader_dashboard, name='reader_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('create_article/', views.create_article, name='create_article'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('search/', views.search, name='search'),
    path('save_article/<int:pk>/', views.save_article, name='save_article'),
 ]