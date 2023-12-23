from django.urls import path

from . import views

app_name = 'item' #acts as a namespace for this application

urlpatterns = [
    path('<int:pk>', views.detail, name='detail'), #expects an int (pk) which has to be same and the ph has to be same as the one in views.py
]