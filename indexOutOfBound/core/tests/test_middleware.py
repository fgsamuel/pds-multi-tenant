import pytest
from django.http import HttpResponse

from core.middlewares import SubdomainTenantMiddleware, get_current_tenant
from django.test import RequestFactory


@pytest.fixture
def fake_view():
    def fake_view(request):
        return HttpResponse('OK')
    return fake_view


def test_tenant_key_thread_local(fake_view):
    tenant_request = RequestFactory(SERVER_NAME='tenant01.com.br').get('/')
    middleware = SubdomainTenantMiddleware(fake_view)
    middleware(tenant_request)
    tenant_key = get_current_tenant()
    assert tenant_key == "tenant01.com.br"


def test_tenant_key_thread_local_with_port(fake_view):
    tenant_request = RequestFactory(SERVER_NAME='tenant01.com.br:8000').get('/')
    middleware = SubdomainTenantMiddleware(fake_view)
    middleware(tenant_request)
    tenant_key = get_current_tenant()
    assert tenant_key == "tenant01.com.br"
