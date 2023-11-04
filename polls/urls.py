from django.urls import path

from . import views

urlpatterns = [
  path("", views.home), 
     
]
urlpatterns =[
     path("", views.index, name="index"),
]