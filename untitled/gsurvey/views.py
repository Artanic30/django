from .models import Site, User
from django.http import HttpResponse
from django.db import transaction
import json
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.core.exceptions import ValidationError


class Sites(View):

    def get(self, request):
        if request.user.is_authenticated:
            result = []
            for i in Site.objects.all():
                result.append({
                    'location': i.location,
                    'time': i.time,
                    'capacity': i.capacity,
                    'student': i.students.count()
                })
            return HttpResponse(json.dumps(result), content_type='application/json')
        else:
            print("request got, user: ", request.user, ". is_authenticated: ", request.user.is_authenticated)
            return HttpResponse(status=403)

    def post(self, request):
        if request.user.is_authenticated:
            user = get_object_or_404(User, name=request.user.username)
            if user.is_activate:
                location = get_object_or_404(Site, location=request.POST.urlencode()[:-1])
                try:
                    with transaction.atomic():
                        user.site_set.clear()
                        location.students.add(user)
                        return HttpResponse('success')
                except ValidationError:
                    return HttpResponse(status=402)
            else:
                return HttpResponse(status=401)
        else:
            print("request got, user: ", request.user, ". is_authenticated: ", request.user.is_authenticated)
            return HttpResponse(status=403)


class Student(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = get_object_or_404(User, name=request.user.name)
            if user.site_set.all().count() == 0:
                result = {
                    'name': user.name,
                    'will': 'empty'
                }
            else:
                result = {
                    'name': user.name,
                    'will': user.site_set.all()[0].location
                }
            return HttpResponse(json.dumps(result), content_type='application/json')
        else:
            print("request got, user: ", request.user, ". is_authenticated: ", request.user.is_authenticated)
            return HttpResponse(status=403)
