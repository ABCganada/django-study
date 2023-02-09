from django.contrib import admin
from django.urls import path, include

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('polls/', include('polls.urls')),
    path('sju/', include('sju.urls')),
]
