from django.urls import path
from . import views

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>', views.read),
    path('update/<id>', views.update),
    path('delete/', views.delete),
]
