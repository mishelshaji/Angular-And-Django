from django.http import request
from django.http.response import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import json
from django.views.decorators.http import require_GET, require_POST
from store.models import Movie

# Create your views here.
@require_GET
def view(request):
    movies = Movie.objects.all()
    serializer = json.Serializer()
    return HttpResponse(serializer.serialize(movies), content_type='application/json')

@require_GET
def view_single(request, id):
    movies = Movie.objects.filter(id=id)
    serializer = json.Serializer()
    return HttpResponse(serializer.serialize(movies), content_type='application/json')

@csrf_exempt
@require_POST
def create(request):
    try:
        m = Movie()
        m.name = request.POST.get("name")
        m.director = request.POST.get("director")
        m.description = request.POST.get("description")
        m.release_date = request.POST.get("release_date")
        m.save()
        return HttpResponse("OK")
    except Exception as e:
        print(e)
        return HttpResponseServerError()

@csrf_exempt
@require_POST
def update(request, id):
    try:
        m = Movie.objects.get(pk=id)
        m.name = request.POST.get("name")
        m.director = request.POST.get("director")
        m.description = request.POST.get("description")
        m.release_date = request.POST.get("release_date")
        m.save()
        return HttpResponse("OK")
    except Exception as e:
        print(e)
        return HttpResponseNotFound()

@require_GET
def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
        movie.delete()
    except Exception as e:
        print(e)
        return HttpResponseNotFound()