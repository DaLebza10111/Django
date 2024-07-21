from django.urls import path
from . import views


#Define the url patterns
urlpatterns = [
    path('', views.index)
]