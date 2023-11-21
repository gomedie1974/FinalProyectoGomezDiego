from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def comienzo(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response