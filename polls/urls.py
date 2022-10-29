from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/', views.update, name = 'update'),
    path('get/', views.get, name = 'get'),
    path('delete/', views.delete, name = 'delete'),
    path('create_choice/', views.create_choice, name='create_choice'),
    path('get_choice/', views.get_choice, name='get_choice'),
    path('update_choice/', views.update_choice, name='update_choice'),
    path('delete_choice/', views.delete_choice, name='delete_choice'),
]