from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import models3d
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request:HttpRequest):
    
    objects = models3d.objects.all()
    print(objects[0].name)
    returnObj = [{"name":object.name, "id":object.id, "url":object.content.url} for object in objects]
    return HttpResponse(json.dumps(returnObj))

def downLoadFile(request:HttpRequest, id):
    object =models3d.objects.get(pk = id)
    print("./.."+object.content.url,object.content)
    file = open("./.."+object.content.url,'rb')
    return HttpResponse(FileWrapper(file))
        
    
@csrf_exempt
def uploadFile(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        files = request.FILES
        file = files.get("file")
        
        uploaded = models3d.objects.create(name = file.name, content = file)
        uploaded.save()
        data = request.FILES
        print(uploaded)
        return HttpResponse("success")