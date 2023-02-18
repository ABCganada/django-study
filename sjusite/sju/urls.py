from django.urls import path
from . import views

# from django.conf import settings
# from django.conf.urls.static import static
app_name = 'sju'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('create/', views.create, name='create'),
    path('semester/create/', views.semester_create, name="semester_create"),
    path('subject/create/<int:sem_id>', views.subject_create, name='subject_create'),
    
    path('read/<int:sem_id>/', views.read, name='read'),
    
    path('semester/update/<int:sem_id>/', views.semester_update, name='semester_update'),
    path('subject/update/<int:sem_id>/', views.subject_update, name='subject_update'),
    
    path('delete/', views.delete, name='delete'),
]
