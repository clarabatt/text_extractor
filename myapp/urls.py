from django.urls import path

from . import views

urlpatterns = [
    path('file_upload/', views.file_upload),
    path('', views.index, name='index'),
]
