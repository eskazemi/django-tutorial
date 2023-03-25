from django.urls import path
from . import views

urlpatterns = [
    path('all_todo/', views.get_all, name='all_todo'),
    path('detail/<int:_id>/', views.detail, name='detail'),
    path('delete/<int:_id>/', views.delete, name='delete'),
]
