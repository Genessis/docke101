import requests

from django.http import HttpResponse
from django.conf import settings
from django.views import View

__all__ = ['EchoView']


class EchoView(View):
    def get(self, request):
        container_response = requests.get(settings.ECHO_URL)
        return HttpResponse(container_response.content)
