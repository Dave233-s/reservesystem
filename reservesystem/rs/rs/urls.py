"""rs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reserve import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('', views.index),
    path('login/', views.login),
    path('logining/', views.logining),
    path('reserve/', views.reserve),
    path('search/', views.search),
    path('ad/', views.ad),
    path('accounts/login/', views.login),
    path('get_r/', views.get_r),
    path('post_status/', views.post_status),
    path('delete_r/', views.delete_r),
    path('put_r/', views.put_r),
    path('post_search/', views.post_search),


]
