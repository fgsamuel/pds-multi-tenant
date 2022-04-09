from core.dbrouter import MultiDatabaseTenantRouter
from core.middlewares import set_current_tenant
from core.models import Tenant


def test_default_db_for_write():
    set_current_tenant("default")
    router = MultiDatabaseTenantRouter()
    assert router.db_for_write(Tenant) == "default"


def test_default_db_for_read():
    set_current_tenant("default")
    router = MultiDatabaseTenantRouter()
    assert router.db_for_read(Tenant) == "default"


def test_domain_db_for_write():
    set_current_tenant("tenant1.com.br")
    router = MultiDatabaseTenantRouter()
    assert router.db_for_write(Tenant) == "tenant1.com.br"


def test_domain_db_for_read():
    set_current_tenant("tenant1.com.br")
    router = MultiDatabaseTenantRouter()
    assert router.db_for_read(Tenant) == "tenant1.com.br"


def test_database_for_write_not_set():
    set_current_tenant("")
    router = MultiDatabaseTenantRouter()
    assert router.db_for_write(Tenant) == ""


def test_database_for_read_not_set():
    set_current_tenant("")
    router = MultiDatabaseTenantRouter()
    assert router.db_for_read(Tenant) == ""
