

from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('JF1860/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('post.urls')),
]
