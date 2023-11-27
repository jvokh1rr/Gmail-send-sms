from django.urls import path
from home import views

urlpatterns = [
    path('', views.example, name='example'),
    path('send_massage/', views.send_massage, name='send_massage')
]