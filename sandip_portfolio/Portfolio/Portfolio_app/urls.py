from django.urls import path
from Portfolio_app import views

urlpatterns = [
    path('',views.index,name='home'),
    path('cert',views.cert,name = 'cert'),
    path('fb',views.fb,name='fb'),
    path('home',views.home,name='home1'),
    path('prjt',views.prjt,name='prjt'),
]