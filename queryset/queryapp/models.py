from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(null=False)
    city = models.CharField(max_length=20)
    mark = models.IntegerField()
    pass_date = models.DateField(max_length=20)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    emp = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=20)
    salary = models.IntegerField()
    join_date = models.DateField(max_length=20)


class Student1(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(null=False)
    city = models.CharField(max_length=20)
    mark = models.IntegerField()
    pass_date = models.DateField(max_length=20)
    adddatetime = models.DateTimeField(max_length=20)

    def __str__(self):
        return self.name
