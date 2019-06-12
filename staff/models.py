from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    b_date = models.DateField(blank=True,null=True)


class Tutor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    vak = models.CharField(max_length=255)
    start_job = models.DateField(blank=True,null=True)
    # appoints = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse('staff:tutor-detail',kwargs={'pk':self.id})

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    group = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    docent = models.ForeignKey(Tutor,on_delete=models.CASCADE,related_name='tut_app')
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='st_app')
    date = models.DateTimeField()

    def __str__(self):
        return "{} apont with docent {} at date {}".format(self.student,self.docent_id,self.date)
