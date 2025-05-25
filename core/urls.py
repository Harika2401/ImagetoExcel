from django.urls import path,include
from core import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
app_name= "core"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginpage, name='userlog'),  # This is what you are missing
    path('userlog/', views.loginpage, name='userlog'),
    path('index/', views.index, name='index'),# if you have this view
    path('upload/', views.upload_file, name='upload_file'),
    path('download/', views.download_file, name='download_file'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)