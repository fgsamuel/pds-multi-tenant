from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    domain_url = models.CharField(max_length=200)
    database_url = models.CharField(max_length=200, unique=True)

    DEFAULT_DB = "default"

    def __str__(self):
        return self.name

    @classmethod
    def db_for(cls, hostname):
        return Tenant.objects.using(cls.DEFAULT_DB).get(domain_url=hostname).database_url

    @classmethod
    def exists(cls, name):
        return Tenant.objects.using(cls.DEFAULT_DB).filter(name=name).exists()
