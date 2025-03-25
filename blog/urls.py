from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', blog_views.post_list, name='post_list'),
    path('register/', blog_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post_list'), name='logout'),
    path('post/create/', blog_views.post_create, name='post_create'),
    path('post/edit/<int:pk>/', blog_views.post_edit, name='post_edit'),
    path('post/delete/<int:pk>/', blog_views.post_delete, name='post_delete'),
]
