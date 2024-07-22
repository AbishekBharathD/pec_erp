from django.contrib import admin

from .models import HOD, CustomUser, Faculty, Student

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(HOD)