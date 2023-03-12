from django.contrib import admin
from .models import PersonalData, Student, Course

# Register your models here.

admin.site.register(PersonalData)
admin.site.register(Student)
admin.site.register(Course)