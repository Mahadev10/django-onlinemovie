from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=200,null=False)
    description=models.TextField(null=False)
    trailer=models.CharField(max_length=200,null=False)
    year=models.IntegerField(null=False)
    star=models.IntegerField(null=False,validators=[MinValueValidator(1),MaxValueValidator(5)])
    show=models.BooleanField(default=True)
    def __str__(self):
        return self.name
