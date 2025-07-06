from django.db import models

class Task2(models.Model):
    username = models.CharField(max_length=150)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)  # You can hash this later
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
