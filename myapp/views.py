from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from .models import Student


def home(request):
    return HttpResponse("Hello, Assessment 1 is working!")


def student_detail(request, student_id):
    return HttpResponse(f"Student ID is: {student_id}")


def average_student_age(request):
    average_age = Student.objects.aggregate(Avg('age'))
    return HttpResponse(average_age)