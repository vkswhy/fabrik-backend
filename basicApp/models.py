from django.db import models

# Create your models here.
class models3d(models.Model):
    name = models.CharField(max_length=25)
    content = models.FileField(upload_to="allModels")