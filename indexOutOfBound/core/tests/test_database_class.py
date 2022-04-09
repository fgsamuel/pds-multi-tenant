import pytest

from django.conf import settings

from core.models import Tenant
from core.tenant_database import Database


def test_return_dict_from_key(db):
    database = Database()
    assert isinstance((database['default']), dict)


def test_cache_dict_from_key(db):
    database = Database()
    database['default']['db_name'] = 'teste'
    assert database['default']['db_name'] == 'teste'


def test_get_backoffice_database_config():
    database = Database()
    assert database['default'] == settings.DATABASE_BACKOFFICE


def test_get_inexistent_database(db):
    database = Database()
    with pytest.raises(KeyError):
        database['inexistent']


def test_get_tenant_connection(db):
    Tenant.objects.using('default').create(name='Tenant 01', domain_url='tenant01.com.br',
                                           database_url='sqlite:///teste.sqlite3')
    database = Database()
    assert database['tenant01.com.br']['NAME'] == 'teste.sqlite3'


def test_default_equal_subdomain(db):
    settings.DATABASE_BACKOFFICE = {'NAME': 'teste.sqlite3'}
    settings.PUBLIC_SUBDOMAIN = 'example.com'
    database = Database()
    assert database["default"] == database["example.com"]
