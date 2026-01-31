
from typing import Any
from django.http import HttpResponseForbidden
from store.models import Store

NOT_ALLOWED_IPS = ["123.45.67.89", "987.56.65.21"]
class IpBlockingMiddleware:

    def __init__(self, get_resposne):
        self.get_response = get_resposne

    def __call__(self, request):
        ip = self.get_client_ip(request)
        if ip in NOT_ALLOWED_IPS:
            return HttpResponseForbidden("Forbidden: IP not allowed")

        return self.get_response(request)
    
    def get_client_ip(self, request) :
        return (
            x_forwarded_for.split(',')[0]
            if (x_forwarded_for := request.META.get('HTTP_X_FORWARDED_FOR'))
            else request.META.get('REMOTE_ADDR')
        )
