from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='LinkHome'),
    path('login/', views.log_in, name='login'),
    path('user/', views.user, name='user'),
    path('logout/', views.log_out, name='logout'),
    path('createbook/', views.create_book, name='createbook'),
    path('user_books/', views.user_books, name='userbooks'),
    path('user_links/<int:id>/', views.user_links, name='userlinks'),
    path('delete_link/<int:id>/', views.delete_link,name='deletelink'),
    path('create_link/', views.create_link, name='createlink'),
    path('delete_book/<int:id>/', views.delete_book, name='deletebook'),
    path('trending/', views.trending, name='trending'),


]