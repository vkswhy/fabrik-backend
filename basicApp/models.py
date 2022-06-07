from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class models3d(models.Model):
    name = models.CharField(max_length=25)
    content = CloudinaryField()