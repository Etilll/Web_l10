from django.urls import path
from noteapp import views
#from .templates.noteapp 
app_name = 'noteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag'),
]