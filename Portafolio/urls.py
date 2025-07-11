from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Any request that is NOT for the admin panel will be sent
    # to the 'projects' app's urls.py file to be handled.
    path('', include('djangoPortafolio.urls')),
]

# This is important for serving user-uploaded media files (like project thumbnails) during development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)