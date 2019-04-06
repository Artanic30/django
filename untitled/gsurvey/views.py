from .models import Site, User
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


class ListView(generic.ListView):
    template_name = 'react/index.html'
    context_object_name = 'sites_list'

    def get_queryset(self):
        return Site.objects.all()
