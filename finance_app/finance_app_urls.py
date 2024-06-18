from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/', include('expenses.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('register/', include('users.urls')),
]
