from django.urls import path
from . import views
from .views import handler404

urlpatterns = [
    path('', views.index, name='sharee')
]
