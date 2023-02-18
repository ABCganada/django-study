from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Semester, Subjects
from .forms import SemesterForm, SubjectsForm

semesters =[
    {'id': 1, 'title': '2018-1(1-1)', 'body': '1학년 1학기는 ...'},
    {'id': 2, 'title': '2018-2(1-2)', 'body': '1학년 2학기는 ...'},
    {'id': 3, 'title': '2019-1(2-1)', 'body': '2학년 1학기는 ...'},
    {'id': 4, 'title': '2021-2(2-2)', 'body': '2학년 2학기는 ...'},
    {'id': 5, 'title': '2022-1(3-1)', 'body': '3학년 1학기는 ...'},
    {'id': 6, 'title': '2022-2(3-2)', 'body': '3학년 2학기는 ...'},
    {'id': 7, 'title': '2023-1(4-1)', 'body': '4학년 1학기는 ...'},
]
nextID = 8


def baseHTML(article, id=None):
    global semesters
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/sju/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
            <li><a href="/sju/update/{id}">update</a></li>
        '''

    ol = ''
    for semester in semesters:
        ol += f'<li><a href="/sju/read/{semester["id"]}">{semester["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/sju/">나는 무슨 수업을 들었나</a></h1>
        <ul>
            {ol}
        </ul>
        <ul>
            {article}
        </ul>
        <ul>
            <li><a href="/sju/create/">create</a></li>
            {contextUI}
        </ul>
    </body>
    </html>
    '''

def index(request):
    semester_list= Semester.objects.order_by('table')
    context = {'semester_list': semester_list}
    return render(request, 'sju/main_page.html', context)

def semester_create(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            semester = form.save(commit=False)
            semester.create_at = timezone.now()
            semester.save()
            return redirect('sju:index')
    else:
        form = SemesterForm()
    context = {'form': form}
    return render(request, 'sju/semester_form.html', context)

def subject_create(request, sem_id):
    semester = get_object_or_404(Semester, pk=sem_id)
    
    if request.method == "POST":
        form = SubjectsForm(request.POST)
        if form.is_valid():
            subjects = form.save(commit=False)
            subjects.create_at = timezone.now()
            subjects.semester = semester
            subjects.save()
            return redirect('sju:read', sem_id=semester.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'semester': semester, 'form':form}
    return redirect(request, 'sju/semester_read.html', context)

@csrf_exempt
def create(request):
    global nextID, semesters
    
    if request.method == 'GET':
        article = '''
            <form action="/sju/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="text"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(baseHTML(article))
    
    elif request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["body"]
        newInfo = {'id': nextID, 'title': title, 'body': content}
        semesters.append(newInfo)
        url = f'/sju/read/{nextID}'
        nextID = nextID + 1
        return redirect(url)

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

@csrf_exempt
def update(request, id):
    global semesters
    
    if request.method == 'GET':
        for semester in semesters:
            if semester['id'] == int(id):
                selected = {'title': semester['title'], 'body': semester['body']}
        
        article = f'''
            <form action="/sju/update/{id}" method="post">
                <p><input type="text" name="title" placeholder="title" value={selected['title']}></p>
                <p><textarea name="body" placeholder="text">{selected['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(baseHTML(article, id))
    
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for semester in semesters:
            if semester['id'] == int(id):
                semester['title'] = title
                semester['body'] = body
        
        
        return redirect(f'/sju/read/{id}')

@csrf_exempt
def delete(request):
    global semesters
    
    if request.method == 'POST':
        id = request.POST['id']
        newInfo = []
        
        for semester in semesters:
            if semester['id'] != int(id):
                newInfo.append(semester)
        semesters = newInfo
        return redirect('/sju/') 