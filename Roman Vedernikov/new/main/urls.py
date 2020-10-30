from django.urls import path, include
from . import views
from django.conf.urls import include, url


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('register', views.RegisterFormView.as_view(), name='register'),
]
