from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('index/', views.index),
    path('list/', views.event_list, name='event_list'),
    path('detail/<int:pk>/', views.event_detail, name='event_detail')
]

