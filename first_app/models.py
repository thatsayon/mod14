from django.db import models

class DModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField() 
    weight = models.FloatField()
    birth_year = models.DateField()