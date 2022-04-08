from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    domain_url = models.URLField()
    database_url = models.CharField(max_length=200, unique=True)

    DEFAULT_DB = "default"

    def __str__(self):
        return self.name

    @classmethod
    def db_for(cls, name):
        return Tenant.objects.using(cls.DEFAULT_DB).get(name=name).database_url

    @classmethod
    def exists(cls, name):
        return Tenant.objects.using(cls.DEFAULT_DB).filter(name=name).exists()

'''
Criar o tenant
usar o default
usar um cara que não existe
'''