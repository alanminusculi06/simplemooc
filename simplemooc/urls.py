from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('simplemooc.core.urls')),
    path('cursos/', include('simplemooc.courses.urls')),
    path('conta/', include('simplemooc.accounts.urls')),
    path('forum/', include('simplemooc.forum.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
