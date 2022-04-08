import pdb
import pytest

from django.conf import settings
from django.db import DatabaseError

from core.models import Tenant
from core.tenant_database import Database


def test_return_dict_from_key():
    database = Database()
    assert type(database['teste']) == dict


def test_cache_dict_from_key():
    database = Database()
    database['teste']['db_name'] = 'teste'
    assert database['teste']['db_name'] == 'teste'


def test_class_always_contains_keys():
    database = Database()
    assert 'teste' in database

# -----------------------------------------------------------------------------


def test_get_backoffice_database_config():
    database = Database()
    assert database['default'] == settings.DATABASE_BACKOFFICE


def test_get_inexistent_database(db):
    database = Database()
    with pytest.raises(KeyError):
        database['inexistent']


def test_get_tenant(db):
    Tenant.objects.using('default').create(name='teste', database_url='sqlite:///teste.sqlite3')
    database = Database()
    assert isinstance(database['teste'], dict)
