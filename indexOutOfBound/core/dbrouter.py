from core.middlewares import get_current_tenant
from core.models import Tenant


def get_tenant(name):
    return Tenant.objects.using('default').get(name=name)


def get_db_for_tenant(name):
    return Tenant.objects.using('default').get(name=name).database_url


class MultiDatabaseTenantRouter:
    @staticmethod
    def db_for_read(model, **hints):
        tenant = get_current_tenant()
        return tenant

    @staticmethod
    def db_for_write(model, **hints):
        tenant = get_current_tenant()
        return tenant
