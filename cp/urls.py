from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.report,name='home'),
    path('report',views.report,name='report'),
    path('predict', views.predict, name="predict") 
]
