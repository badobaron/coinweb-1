from django.urls import path
from . import views

urlpatterns =[
	path('',views.index, name='index'),
	path('get_log/', views.get_log, name='get_log'),
]