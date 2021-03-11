from django.shortcuts import render, redirect
from .models import Student

# Retrieve / Read (조회)
def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'orm_practice/index.html', context)


def detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {'student': student}
    return render(request, 'orm_practice/detail.html', context)


# Create (생성)
def new(request):
    return render(request, 'orm_practice/new.html')


def create(request):
    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.major = request.POST.get('major')
        student.intro = request.POST.get('intro')
        student.save()
        # redirect(RAW URL / urls.py 의 name)
        return redirect('detail', pk=student.pk)
    return redirect('new')

# Update
## 수정용 HTML 제공
def edit(request, pk):
    student = Student.objects.get(pk=pk)
    context = {'student': student}
    return render(request, 'orm_practice/edit.html', context)

## 실제 수정
def update(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.major = request.POST.get('major')
        student.intro = request.POST.get('intro')
        student.save()
        return redirect('detail', pk = student.pk)
    return redirect('edit', pk=pk)

# Delete
def delete(request):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.delete()
        return redirect('index')
    return redirect('detail', pk=pk)