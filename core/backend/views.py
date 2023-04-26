# from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Page
# Create your views here.


def index(request):
    return TemplateResponse(
        request,
        'backend/index.html',
        {'obj': Page.objects.all()}
    )
