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

