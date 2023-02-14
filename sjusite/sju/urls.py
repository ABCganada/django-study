from django.urls import path
from . import views

# from django.conf import settings
# from django.conf.urls.static import static
app_name = 'sju'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('subject/create/<int:sem_id>/', views.subject_create, name='subject_create'),
    path('read/<int:sem_id>/', views.read, name='read'),
    path('update/<id>/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
