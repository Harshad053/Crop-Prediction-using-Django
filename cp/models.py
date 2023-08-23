from django.db import models

# Create your models here.
class CropData(models.Model):
    N=models.IntegerField()
    P=models.IntegerField()
    K=models.IntegerField()
    temperature=models.FloatField()
    humidity=models.FloatField()
    ph=models.FloatField()
    rainfall=models.FloatField()
    result=models.TextField()

    def __str__(self):
        return self.result