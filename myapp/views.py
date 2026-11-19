from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from .models import Student

def average_student_age(request):
    average_age = Student.objects.aggregate(Avg('age'))
    return HttpResponse(average_age)