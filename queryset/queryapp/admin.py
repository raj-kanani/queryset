from django.contrib import admin
from .models import Student, Teacher, Student1


@admin.register(Student)
class studentadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'mark', 'pass_date']


@admin.register(Student1)
class Student1admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'mark', 'pass_date', 'adddatetime']


@admin.register(Teacher)
class Teachertadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'emp', 'city', 'salary', 'join_date']
