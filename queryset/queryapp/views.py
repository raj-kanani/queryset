from django.db.models import Q, Avg, Sum, Min, Max,Count
from django.shortcuts import render

# Create your views here.
from .models import student, teacher, student1


#######  1) QUERYSET API WITH RETURN OBJECT.........................
def home(request):
    # s = student.objects.all()

    # s = student.objects.filter(mark=62, city='rajkot')
    # s = student.objects.exclude(mark=60)
    # s = student.objects.order_by('name')
    # s = student.objects.order_by('id').reverse()[0:4]
    # s = student.objects.values('name', 'city')
    # s = student.objects.values_list('id', 'name', named=True)
    # s = student.objects.using('default')# same as all method...
    # s = student.objects.dates('pass_date', 'year')

    ##### union , intersection, diffrence..........................................
    # s1 = student.objects.values_list('id', 'name', named=True)
    # s2 = teacher.objects.values_list('id', 'name', named=True)
    # s = s2.union(s1, all=True)
    # s1 = student.objects.values_list('id', 'name', named=True)
    # s2 = teacher.objects.values_list('id', 'name', named=True)
    # s = s2.intersection(s1)
    # s1 = student.objects.values_list('id', 'name', named=True)
    # s2 = teacher.objects.values_list('id', 'name', named=True)
    # s = s1.difference(s2)

    ############## AND OR operator.........(Q queryset)
    # s = student.objects.filter(id=4) & student.objects.filter(name='ravi')
    # s = student.objects.filter(Q(id=4) & Q(name='ravi'))
    s = student.objects.filter(Q(id=4) | Q(name='rutvik'))
    # s = student.objects.filter(id=4) | student.objects.filter(name='raj')
    print('return :', s)
    print('sql query:', s.query)
    return render(request, 'home.html', {'s': s})

####### 2) QUERYSET API WITH DONT RETRUN OBJECTS................

def index(request):
    # s = student.objects.get(id=1)
    # s = student.objects.first()
    # s = student.objects.last()
    # s = student.objects.latest('pass_date')
    # s = student.objects.earliest('pass_date')
    # s = student.objects.exists()# return true
    # print(s.exists())
    # s = student.objects.order_by('-name').first()
    ######### CRUD method...........
    # s = student.objects.create(name='rk')
    # s = student.objects.filter(mark=60).update(city='jaipur')
    # s, created = student.objects.update_or_create(id=4, name='ram', defaults={'name': 'ravibhai'})
    # s, created = student.objects.get_or_create()
    # obj = [
    #     student(name='rajesh', roll=108, city='junagadh', mark=88, pass_date='2022-3-10'),
    #     student(name='rohit', roll=109, city='junagadh', mark=58, pass_date='2022-3-18'),
    #     student(name='rajat', roll=111, city='rajkot', mark=88, pass_date='2022-3-17')
    #
    # ]
    # s = student.objects.bulk_create(obj)
######## update bult data........
    # data = student.objects.all()
    # for stu in data:
    #     stu.city = 'ahmedabad'
    # s = student.objects.bulk_update(data, ['city'])
##### data get....
    # s = student.objects.in_bulk([1, 2])# terminal name get
    # print(s[1].name)
    # print(s[2].name)
####### delete operation..........
    # s = student.objects.get(id=12).delete()
    # s = student.objects.all().delete() #### all data delete

###### count data ...
    s = student.objects.count()
    print('total data :', s)
    # print('create :', created)
    # print('sql query:', s.query)
    return render(request, 'index.html', {'s': s})


########### 3) QUERYSET API FIELD LOOKUP.............

def base(request):
    # s = student1.objects.all()
    # s = student1.objects.filter(name__exact='raj') # capital, small check kri print kre
    # s = student1.objects.filter(name__iexact='RaHUL') # name match ,doesnot matter capital or smnall
    # s = student1.objects.filter(name__contains='A') #check r and r-name data print
    # s = student1.objects.filter(name__icontains='A') #check r and r-name data print
    # s = student1.objects.filter(mark__in=[65]) # check in or not
    # s = student1.objects.filter(mark__gt=65) # check 65+ mark data
    # s = student1.objects.filter(mark__gte=75) # greater than or equal
    # s = student1.objects.filter(mark__lt=75) # less than
    # s = student1.objects.filter(name__startswith='a') # start a name
    # s = student1.objects.filter(name__istartswith='R') # start R name with case insensitive
    # s = student1.objects.filter(name__endswith='H') # start a name with case sensitive
    # s = student1.objects.filter(pass_date__range=('2022-03-1', '2022-03-10')) # date between data show
    s = student1.objects.filter(pass_date__month=3) # 3 month  data show
    print('return :', s)
    print('query : ', s.query)
    return render(request, 'base.html', {'s': s})

###### 4) aggregation
def base2(request):
    s = student.objects.all()
    a = s.aggregate(Avg('mark'))# perform average marks
    sum = s.aggregate(Sum('mark'))
    min = s.aggregate(Min('mark'))
    max = s.aggregate(Max('mark'))
    count = s.aggregate(Count('mark'))
    c = {'s': s, 'a': a, 'sum': sum, 'min': min, 'max': max, 'count': count}
    print('total average :', a)
    print('return :', s)
    print('query : ', s.query)
    return render(request, 'base2.html', c)


#############  5) Q object (AND, OR, NOR.....

# s = student.objects.filter(Q(id=6) & Q(roll=106)) #AND
# s = student.objects.filter(Q(id=6) | Q(roll=108)) # OR
# s = student.objects.filter(~Q(id=60)) # NOR