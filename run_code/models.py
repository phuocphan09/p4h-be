from django.db import models

# Create your models here.


class RunPythonCode(models.Model):
    error = models.IntegerField()
    msg = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
