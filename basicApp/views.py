from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import models3d
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request:HttpRequest):
    try:
        objects = models3d.objects.all()
        returnObj = [{"name":object.name, "id":object.id, "url":object.content.url} for object in objects]
        return HttpResponse(json.dumps(returnObj))
    except:
        return HttpResponse("some error occured")

def downLoadFile(request:HttpRequest, id):
    try:
        object =models3d.objects.get(pk = id)
        file = open("./.."+object.content.url,'rb')
        return HttpResponse(FileWrapper(file))
    except:
        return HttpResponse("some error occured")        
    
@csrf_exempt
def uploadFile(request: HttpRequest):
    try:
        if request.method == "POST":
            data = request.POST
            files = request.FILES
            file = files.get("file")
            
            uploaded = models3d.objects.create(name = file.name, content = file)
            uploaded.save()
            data = request.FILES
            return HttpResponse("success")
    except:
        return HttpResponse("some error occured")