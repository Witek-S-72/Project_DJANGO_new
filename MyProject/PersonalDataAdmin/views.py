from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import PersonalData, Student

def personal_data_list(request):
    personaldata = PersonalData.objects.all()
    ctx = {'personaldata':personaldata}
    return render(request, 'PersonalDataAdmin/personal_data_list.html',ctx)

def personal_data_detail(request, id):
    try:
        personaldata = PersonalData.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    ctx = {'personaldata':personaldata}
    return render(request, 'PersonalDataAdmin/personal_data_detail.html', ctx)

def student_list(request):
    student = Student.objects.all()
    ctx = {'student':student}
    return render(request, 'PersonalDataAdmin/student_list.html', ctx)

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    ctx = {'student':student}
    return render(request, 'PersonalDataAdmin/student_detail.html', ctx)








