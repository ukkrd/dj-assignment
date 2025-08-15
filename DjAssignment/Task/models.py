from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(blank=True, null=True)  
    completed = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

