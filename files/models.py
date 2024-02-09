from django.db import models
from django.utils import timezone


def file_generate_upload_path(instance, filename):
    return f"files/{instance.file_name}"


class FileStorage(models.Model):
    file = models.FileField(upload_to='files/')
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file.name

