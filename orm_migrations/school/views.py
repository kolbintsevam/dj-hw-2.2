from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    p = Student.objects.all().prefetch_related('teachers')
    context = {'object_list': p}
    return render(request, template, context)