from django.urls import path     
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('registration', views.registration),
    path('signin', views.signin),
    path('login', views.login),
    path('logout', views.logout),

    path('home', views.index),
#     path('trips/new', views.new),
#     path('trips/create', views.create),
#     path('trips/edit/<int:id>', views.edit),
#     path('trips/<int:id>/update', views.update),
#     path('trips/<int:id>', views.show),
#     path('trips/<int:id>/delete', views.delete),
] 
urlpatterns += staticfiles_urlpatterns()