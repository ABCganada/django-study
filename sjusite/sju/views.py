from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Semester, Subjects
from .forms import SemesterForm, SubjectsForm

def index(request):
    semester_list= Semester.objects.order_by('table')
    context = {'semester_list': semester_list}
    return render(request, 'sju/main_page.html', context)

def semester_create(request):
    
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            sem = form.save(commit=False)
            sem.create_at = timezone.now()
            sem.save()
            return redirect('sju:index') 
    else:
        form = SemesterForm()
    context = {'form': form}
    return render(request, 'sju/semester_form.html', context)

def subject_create(request, sem_id):
    sem = get_object_or_404(Semester, pk=sem_id)
    
    if request.method == "POST":
        form = SubjectsForm(request.POST)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.create_at = timezone.now()
            sub.semester = sem
            sub.save()
            # if result:
            #     semester.credits += subjects.credit
            #     semester.save()
            
            return redirect('sju:read', sem_id=sem.id)
    else:
        form = SubjectsForm()
    context = {'semester': sem, 'form': form}
    return render(request, 'sju/subjects_form.html', context)

def read(request, sem_id):
    sem = get_object_or_404(Semester, pk=sem_id)
    context = {'sem': sem}
    return render(request, 'sju/semester_read.html', context)
    
    
    # global semesters
    # article = ''
    # for semester in semesters:
    #     if semester['id'] == int(id):
    #         article = f'<h2>{semester["title"]}</h2>{semester["body"]}'
    #         break
        
    # return HttpResponse(baseHTML(article, id))

def semester_update(request, sem_id):
    sem = get_object_or_404(Semester, pk=sem_id)
    
    if request.method == "POST":
        form = SemesterForm(request.POST, instance=sem)
        if form.is_valid():
            sem = form.save(commit=False)
            sem.update_at = timezone.now()
            sem.save()
            return redirect('sju:read', sem_id = sem.id)
    else:
        form = SemesterForm(instance=sem)
    context = {'form': form}
    return render(request, 'sju/semester_form.html', context)

def subject_update(request, sem_id):
    sub = get_object_or_404(Subjects, pk=sem_id)
    
    if request.method == "POST":
        form = SubjectsForm(request.POST, instance=sub)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.update_at = timezone.now()
            sub.save()
            return redirect('sju:read', sem_id=sub.semester.id)
    else:
        form = SubjectsForm(instance=sub)
    context = {'subjects': sub, 'form': form}
    return render(request, 'sju/subjects_form.html', context)

def semester_delete(request, sem_id):
    sem = get_object_or_404(Semester, pk=sem_id)
    
    sem.delete()
    return redirect('sju:index')

def subject_delete(request, sem_id):
    sub = get_object_or_404(Subjects, pk=sem_id)
    
    sub.delete()
    return redirect('sju:read', sem_id=sub.semester.id)