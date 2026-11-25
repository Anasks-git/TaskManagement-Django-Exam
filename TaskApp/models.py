from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskDB(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20,default="pending")

    def __str__(self):
        return self.title

