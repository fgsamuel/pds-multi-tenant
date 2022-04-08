from core.middlewares import get_current_tenant
from core.models import Tenant
from django.conf import settings


def get_tenant(name):
    return Tenant.objects.using('default').get(name=name)

def get_db_for_tenant(name):
    return Tenant.objects.using('default').get(name=name).database_url

class MultiDatabaseTenantRouter:
    def db_for_read(self, model, **hints):
        tenant = get_current_tenant()
        if not tenant:  # We're on the backoffice.
            return settings.DATABASES["default"]

        return settings.DATABASES[tenant]

    def db_for_write(self, model, **hints):
        return get_current_db_name()

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Just migrate tenant model on default db
        if model_name == 'tenant' and db != 'default':
            return False
        return None