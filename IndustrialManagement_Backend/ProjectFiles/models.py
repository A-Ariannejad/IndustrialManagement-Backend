import os
from django.db import models
from django.core.exceptions import ValidationError
from Projects.models import CustomUser, Project
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.ppt', '.pptx', '.doc', '.docx', '.zip', '.rar', '.jpg', '.png']
    if ext.lower() not in valid_extensions:
        raise ValidationError(f'Unsupported file extension: {ext}. Allowed extensions are {", ".join(valid_extensions)}')

class ProjectFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/', validators=[validate_file_extension])
    uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
