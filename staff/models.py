from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    b_date = models.DateField(blank=True,null=True)


class Tutor(User):
    vak = models.CharField(max_length=255)
    start_job = models.DateField(blank=True,null=True)


    def __str__(self):
        return self.last_name

class Student(User):
    group = models.PositiveIntegerField()

    def __str__(self):
        return self.last_name
