from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=155,blank=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title