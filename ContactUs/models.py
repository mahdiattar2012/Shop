from django.db import models
from django.db.models.base import Model
from .managers import ContactManager

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    subject = models.CharField(max_length=80)
    message = models.TextField(max_length=500)
    create = models.DateTimeField(auto_now_add=True)
    objects = ContactManager()

    def __str__(self):
        return self.subject
