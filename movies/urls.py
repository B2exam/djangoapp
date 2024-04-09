
from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index),
    path('<int:pk>', views.detail),
    path('<int:pk>/delete', views.delete),
    path('<int:pk>/update', views.update),
    path('create', views.create)
]