from django.shortcuts import render
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# Create your views here.

def index(request):
    context = {'segment':'clients'}

    html_template = loader.get_template('clients/manage-clients.html')
    return HttpResponse(html_template.render(context, request))
    # return HttpResponse('Testando lista de clientes')
