from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import TemplateView
from .views import FileUploadView

urlpatterns = [
    path('', FileUploadView.as_view(), name='file-upload'),
    path('success/', TemplateView.as_view(template_name='files/success.html'), name='success'),
]
