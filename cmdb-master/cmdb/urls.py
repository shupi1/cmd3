"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path, include
from app import views
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('login/', views.user_login),
    path('admin/', admin.site.urls),
    # path('register/', views.user_register),
    path('logout/', views.user_logout),
    path('dashboard/', views.dashboard),
    path('users/', include('users.urls')),
    path('assets/', include('assets.urls')),
]
