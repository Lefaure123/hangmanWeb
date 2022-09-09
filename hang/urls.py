from django.urls import path
from . import views 

urlpatterns = [
    path('', views.akey, name='akey'),
    path('enskri/', views.enskripsyon, name='enskri'),
    path('konekte/', views.koneksyon, name='konekte')
]
