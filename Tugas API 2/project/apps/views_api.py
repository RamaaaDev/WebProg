from django.shortcuts import render, redirect
from django.http import JsonResponse
from apps.models import Course
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
import requests


@csrf_exempt
def apiCourse(request):
    if request.method == "GET":
        data = serializers.serialize("json", Course.objects.all())
        return JsonResponse(json.loads(data), safe=False)

    if request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))
        if not body:
            return JsonResponse({"message": "data is not json type!"}, safe=False)
        else:
            created = Course.objects.create(
                course_name=body.get('course_name', '')  # Use .get() to avoid KeyError
            )
            return JsonResponse({"message": "data successfully created!"}, safe=False)

    if request.method == "PUT":
        body = json.loads(request.body.decode("utf-8"))
        course_id = body.get('id')
        new_course_name = body.get('course_name')
        
        if not course_id or not new_course_name:
            return JsonResponse({"message": "Missing ID or course_name!"}, safe=False)
        
        try:
            course = Course.objects.get(id=course_id)
            course.course_name = new_course_name
            course.save()
            return JsonResponse({"message": "data successfully updated!"}, safe=False)
        except Course.DoesNotExist:
            return JsonResponse({"message": "Course not found!"}, safe=False)

    if request.method == "DELETE":
        body = json.loads(request.body.decode("utf-8"))
       
        course_id = body.get('id')
        
        if not course_id:
            return JsonResponse({"message": "ID is required!"}, safe=False)
        
        try:
            course = Course.objects.get(id=course_id)
            course.delete()
            return JsonResponse({"message": "data successfully deleted!"}, safe=False)
        except Course.DoesNotExist:
            return JsonResponse({"message": "Course not found!"}, safe=False)
@csrf_exempt
def consumeApiGet(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    return render(request, "api-get.html", {'data': data})

@csrf_exempt
def consumeApiPost(request):
    if request.method == "POST":
        payload = {
            "name": request.POST.get("name"),
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "address": {
                "street": request.POST.get("street"),
                "suite": request.POST.get("suite"),
                "city": request.POST.get("city"),
                "zipcode": request.POST.get("zipcode"),
                "geo": {
                    "lat": request.POST.get("lat"),
                    "lng": request.POST.get("lng")
                }
            },
            "phone": request.POST.get("phone"),
            "website": request.POST.get("website"),
            "company": {
                "name": request.POST.get("company_name"),
                "catchPhrase": request.POST.get("catchPhrase"),
                "bs": request.POST.get("bs")
            }
        }

        post_url = "https://jsonplaceholder.typicode.com/posts"
        
        post_response = requests.post(post_url, json=payload)
        
        if post_response.status_code == 201:
            messages.success(request, 'Data berhasil dikirim!')
        else:
            messages.error(request, 'Gagal mengirim data. Status code: {}'.format(post_response.status_code))
        
        return redirect('apps:api-consume-get-data')
    
    return render(request, "api-post.html")
    

