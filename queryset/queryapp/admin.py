from django.contrib import admin

# Register your models here.
from .models import student, teacher,student1


@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'mark', 'pass_date']


@admin.register(student1)
class student1admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'mark', 'pass_date', 'adddatetime']

@admin.register(teacher)
class teachertadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'emp', 'city', 'salary', 'join_date']
