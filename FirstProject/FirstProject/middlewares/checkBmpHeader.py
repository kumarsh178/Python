
from typing import Any
from django.http import HttpResponseForbidden # type: ignore
from store.models import Store

class CheckBMPHeader:

    def __init__(self, get_resposne):
        self.get_response = get_resposne

    def __call__(self, request):
        headers = request.headers
        bmpId = headers.get("bmp")
        """if "bmp" not in headers:
            return HttpResponseForbidden("Missing: Header Bmp")
        else:
            if not Store.objects.filter(bmp_id=bmpId).exists():
                return HttpResponseForbidden("Invalid Bmp")"""

        return self.get_response(request)