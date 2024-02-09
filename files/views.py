import os
import boto3
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from .forms import FileUploadForm
from .models import FileStorage
from file_upload_task import settings


class FileUploadView(CreateView):
    model = FileStorage
    template_name = 'files/upload_file.html'
    form_class = FileUploadForm
    success_url = reverse_lazy('success')

    def post(self, request, *args, **kwargs):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            s3 = boto3.client(
                's3',
                aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
            )

            img_url = f"{settings.MEDIA_ROOT}/{form.instance.file.name}"
            s3.upload_file(img_url, os.environ.get("AWS_S3_BUCKET_NAME"), form.instance.file.url)

            return redirect(self.success_url)
        return render(request, self.template_name)
