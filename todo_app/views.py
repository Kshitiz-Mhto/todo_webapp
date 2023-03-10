from django.shortcuts import render, redirect
from .models import Todo_app,userTask
import time
# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def login(request):
    return render(request,'login.html')

def entry(request):
    return render(request, 'signup.html')

def user_creation(request):
    name = request.POST['fullname']
    usr_name = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    x = Todo_app.objects.create(fullname=name,username=usr_name,email=email,password=password)
    if x:
        x.save()
    time.sleep(5)
    return render(request,'login.html', {'username':usr_name,'password':password})
    
def logind(request):
    usr_name = request.POST['username']
    password = request.POST['password']
    print(usr_name,password)
    users = Todo_app.objects.all()
   
    # evenlist = list(filter(lambda x: x.username == usr_name,users))
    # for i in evenlist:
    #     print (i)
    
    for x in users:
        if(x.username == usr_name and x.password == password):
            return render(request,'welcome.html')
    return redirect('login')

def workspace(request,username):
    usr_name = request.POST['username']
    password = request.POST['password']
    # print(usr_name,password)
    obj = Todo_app.objects.all()
    msg = "Credential are wrong!"
    for x in obj:
        if(x.username == usr_name and x.password == password):
            return render(request,'workspace.html', {'user':username})
    return render(request, 'login.html', {'msg': msg})

def workspaceHome(request,username):
    return render(request,'workspace.html', {'user':username})

def workspaceTask(request,username):
    tasks = userTask.objects.all()
    if (tasks.exists()):
        return render(request,'tasks.html', {'user':username, 'tasks':tasks})
    return render(request,'tasks.html', {'user':username})
def taskSaved(request, username):
    title_id = request.POST['title_id']
    title = request.POST['title']
    detail = request.POST['detail']
    obj = userTask.objects.create(title_id=title_id,title=title, detail = detail)
    if obj:
        obj.save()
    time.sleep(1)
    tasks = userTask.objects.all()
    for x in tasks:
        print(x)
    return render(request,'tasks.html', {'user':username, 'tasks':tasks})

def taskDelete(request, title_id):
    obj = userTask.objects.get(title_id)
    obj.delete()
    tasks = userTask.objects.all()
    if (tasks.exists()):
        return render(request,'tasks.html', { 'tasks':tasks})
    return render(request,'tasks.html')

def taskEdit(request, title_id):
    obj = userTask.objecs.get(title_id)
    
    return redirect('/wrokspaceTask/')