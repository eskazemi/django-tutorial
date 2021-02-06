from django.urls import path
from .import views

urlpatterns=[
    path('hello/',views.sayhello,name='hello'),
    path('all_todo/',views.all_todo,name='all_todo'),
    path('detail/<int:id>/',views.detail,name='detail'),
]