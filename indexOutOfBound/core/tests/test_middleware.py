# import pytest
# from django.http import HttpResponse
#
# from core.middlewares import TenantMiddleware
# from django.test import RequestFactory
#
#
# # Tenant
# # subdomain -> tenant01
# # dbstring ->
# from core.models import Tenant
#
#
# @pytest.fixture
# def tenant_request():
#     factory = RequestFactory(SERVER_NAME='tenant01.com.br')
#     return factory.get('/')
#
#
# def test_set_db_for_router(tenant_request, db, mocker):
#
#     Tenant.objects.create(name='tenant01', database_url='sqlite:///tenant01.com.br.sqlite3',
#                           domain_url='tenant01.com.br')
#
#     mock = mocker.patch('core.middlewares.set_db_for_router')
#
#     def fake_view(request):
#         return HttpResponse()
#
#     middleware = TenantMiddleware(fake_view)
#     result = middleware(tenant_request)
#     print(result)
#
#     mock.assert_called_once_with('tenant01.com.br.sqlite3')
