from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Tenant
from django.core.management import call_command


@receiver(post_save, sender=Tenant)
def handle_tenant_created(sender, instance, created, **kwargs):
    if created:
        call_command('migrate', database=instance.database_url)
