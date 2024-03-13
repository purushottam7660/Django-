from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    marks=models.IntegerField()
    address=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    # def __str__(self):
    #     return self.name


