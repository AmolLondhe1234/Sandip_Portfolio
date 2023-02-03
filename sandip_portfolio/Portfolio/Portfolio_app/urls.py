from django.urls import path
from Portfolio_app import views

urlpatterns = [
    path('',views.index,name='home')
]