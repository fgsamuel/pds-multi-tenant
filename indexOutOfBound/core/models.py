from django.core.management import call_command
from django.db import models

# Create your models here.


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    domain_url = models.CharField(max_length=300)
    database_url = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
