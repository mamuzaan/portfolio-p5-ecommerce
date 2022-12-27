from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sharee')
]

handler404 = 'sharee.views.handler404'
