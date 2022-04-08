import threading


THREAD_LOCAL = threading.local()


def set_current_tenant(name):
    setattr(THREAD_LOCAL, "tenant", name)


def get_current_tenant():
    return getattr(THREAD_LOCAL, "tenant", "")


class BaseTenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant = self.tenant_from_request(request)
        set_current_tenant(tenant)

        return self.get_response(request)

    @staticmethod
    def tenant_from_request(request):
        raise NotImplemented


class PathTenantMiddleware(BaseTenantMiddleware):
    @staticmethod
    def tenant_from_request(request):
        if request.path.startswith('/tenants/'):
            return request.path.split('/')[2]
        return None


class SubdomainTenantMiddleware(BaseTenantMiddleware):
    @staticmethod
    def tenant_from_request(request):
        return request.get_host().split(':')[0]


class DomainTenantMiddleware(BaseTenantMiddleware):
    @staticmethod
    def tenant_from_request(request):
        ...
