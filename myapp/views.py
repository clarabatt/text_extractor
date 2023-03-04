from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def handle_uploaded_file(f):
    file_name = f.name
    print(f)
    with open('myapp/static/media/'+file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_name
