from django.db import models
# Create your models here.


class table(models.Model):
    id=models.AutoField(primary_key=True)
    lat=models.FloatField()
    lon=models.FloatField()
