from django.db import models
from users.models import CustomUser
# Create your models here.

class Project(models.Model):
    title= models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by= models.ForeignKey(CustomUser,
    related_name='projects',
    on_delete=models.SET_NULL,
    null=True,
    blank=True)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        creator = self.created_by.email if self.created_by else "Unknown"
        return f" {self.title} created by {creator} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"