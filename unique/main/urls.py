from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='site-home'),
    path('home', views.home, name='site-home'),
    path('memberships', views.memberships, name='site-memberships'),
    path('training', views.training, name='site-training'),
    path('services', views.services, name='site-services')
]
