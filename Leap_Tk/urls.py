from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('UserApp.urls')), 
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('Answer/', include('TkApp.urls')), 
    path('myadmin/', include('My_Admin.urls') ,name = "myadmin"), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
