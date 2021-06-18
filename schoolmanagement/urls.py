
from django.contrib import admin
from django.urls import path, include
from .views import home_page
from teacher.views import teacher_registration
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('teacher/', include('teacher.urls')),
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
