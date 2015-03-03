from models import * 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def list(request):
    return object_list(request,
            queryset=Forecaster.objects.all(),
            paginate_by=50, allow_empty=True)


def detail(request, slug):
    return object_detail(request,
            queryset=Forecaster.objects.all(),
            slug=slug, slug_field='slug')