from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('polls_app.urls')),
    path('admin/', admin.site.urls),
    path('polls_django/', include('polls.urls')),
]
