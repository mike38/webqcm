# Create your views here.
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from associate.models import Copie, Etudiant, Associate

def index(request):
    Copie_list = Copie.objects.all()
    return render_to_response('associate/index.html', {'Copie_list': Copie_list })

def copie(request, copie_id):
    return HttpResponse("You're looking at Copie %s." % copie_id)
