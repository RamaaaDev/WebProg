from django.shortcuts import render
from django.http import JsonResponse
from apps.models import Course
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def apiCourse(request):
    if request.method == "GET":
        # Serialize the data into JSON
        data = serializers.serialize("json", Course.objects.all())
        # Turn the JSON data into a dict and send as JSON response
        return JsonResponse(json.loads(data), safe=False)

    if request.method == "POST":
        # Turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
        # Filter data
        if not body:
            return JsonResponse({"message": "data is not json type!"}, safe=False)
        else:
            created = Course.objects.create(
                course_name=body.get('course_name', '')  # Use .get() to avoid KeyError
            )
            return JsonResponse({"message": "data successfully created!"}, safe=False)

    if request.method == "PUT":
        # Turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
        # Retrieve the ID and data to update
        course_id = body.get('id')
        new_course_name = body.get('course_name')
        
        if not course_id or not new_course_name:
            return JsonResponse({"message": "Missing ID or course_name!"}, safe=False)
        
        try:
            # Fetch the course and update it
            course = Course.objects.get(id=course_id)
            course.course_name = new_course_name
            course.save()
            return JsonResponse({"message": "data successfully updated!"}, safe=False)
        except Course.DoesNotExist:
            return JsonResponse({"message": "Course not found!"}, safe=False)

    if request.method == "DELETE":
        # Turn the body into a dict
        body = json.loads(request.body.decode("utf-8"))
        # Retrieve the ID to delete
        course_id = body.get('id')
        
        if not course_id:
            return JsonResponse({"message": "ID is required!"}, safe=False)
        
        try:
            # Fetch the course and delete it
            course = Course.objects.get(id=course_id)
            course.delete()
            return JsonResponse({"message": "data successfully deleted!"}, safe=False)
        except Course.DoesNotExist:
            return JsonResponse({"message": "Course not found!"}, safe=False)
        

