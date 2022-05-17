from django.urls import path
from . import views # 같은 폴더 내의 views.py를 import
from django.conf import settings # cv_project의 settings.py
from django.conf.urls.static import static


app_name = 'opencv_webapp'

urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('detect_face/', views.detect_face, name='detect_face'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
