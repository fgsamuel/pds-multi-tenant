import dj_database_url
from django.conf import settings


class Database(dict):
    cache = {}

    def __getitem__(self, tenant):
        if tenant == settings.PUBLIC_SUBDOMAIN or tenant == 'default':
            return settings.DATABASE_BACKOFFICE
        if tenant not in self.cache:
            from core.models import Tenant
            try:
                db_url = Tenant.db_for(tenant)
            except Tenant.DoesNotExist:
                raise KeyError(tenant)
            self.cache[tenant] = dj_database_url.parse(db_url)
        return self.cache[tenant]

    def __contains__(self, tenant):
        return True
