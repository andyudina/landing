from django.shortcuts import render
from django.http import HttpResponse
from models import Lead
import json
# Create your views here.
MIN_EMAIL_LEN = 5

def index(request):
    return render(request, 'landing/index.html')

def email_ajax(request):
    try:
        email = request.GET['email']
        if len(email) < MIN_EMAIL_LEN:
            raise Exception
        Lead.objects.create(email=email)
        print Lead.objects.all()
        return HttpResponse(json.dumps({'resultFlag': True}))
    except Exception:
        return HttpResponse(json.dumps({'resultFlag': False}))
