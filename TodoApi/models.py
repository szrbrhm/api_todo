from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    TITLE = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    )
    priority = models.CharField(max_length=50, choices=TITLE, default='L')
    
    done = models.BooleanField(default=False)
    updatedDate = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task


    
